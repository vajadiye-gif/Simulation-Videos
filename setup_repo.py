#!/usr/bin/env python3
"""
Generate a GitHub-ready repo skeleton for simulation videos.

Layout:
    videos/tuple_XX_ka{a}_kg{g}/params.json
    videos/tuple_XX_ka{a}_kg{g}/run_1.mp4 ... run_3.mp4   (you add these)
    videos/README.md (Drive link), manifest.csv, README.md, .gitattributes, .gitignore
"""
import csv
import json
from pathlib import Path

ROOT = Path("simulation-videos")   # repo folder name
N_RUNS = 3                         # videos per tuple
K_VALUES = range(5)                # k = 0..4

# Paste your Drive folder link here (Share -> Anyone with the link -> Viewer)
DRIVE_LINK = "https://drive.google.com/drive/folders/1WyvIvhv-h80lf_WhIfWipEAfWuK6Ef2r?usp=sharing"


def make_params(k_alpha, k_gamma):
    """Parameter set from Eq. (12); alpha's use k_alpha, gamma's use k_gamma."""
    return {
        "alpha1": k_alpha + 0.5,
        "alpha2": k_alpha + 0.2,
        "gamma11": k_gamma + 0.2,
        "gamma12": k_gamma + 0.5,
        "gamma22": k_gamma + 0.8,
    }


def main():
    # Build the 25 tuples with explicit loops
    tuples = []
    idx = 1
    for k_alpha in K_VALUES:
        for k_gamma in K_VALUES:
            tuples.append({
                "id": idx,
                "name": f"tuple_{idx:02d}_ka{k_alpha}_kg{k_gamma}",
                "k_alpha": k_alpha,
                "k_gamma": k_gamma,
                "params": make_params(k_alpha, k_gamma),
            })
            idx += 1

    videos_dir = ROOT / "videos"
    videos_dir.mkdir(parents=True, exist_ok=True)

    manifest_rows = []
    for t in tuples:
        folder = videos_dir / t["name"]
        folder.mkdir(exist_ok=True)

        # Per-tuple parameter file
        with open(folder / "params.json", "w") as f:
            json.dump({"k_alpha": t["k_alpha"], "k_gamma": t["k_gamma"],
                       **t["params"]}, f, indent=2)

        # .gitkeep so empty folders are tracked until videos are added
        (folder / ".gitkeep").touch()

        for run in range(1, N_RUNS + 1):
            manifest_rows.append({
                "tuple_id": t["id"],
                "k_alpha": t["k_alpha"],
                "k_gamma": t["k_gamma"],
                **t["params"],
                "run": run,
                "video_path": f"videos/{t['name']}/run_{run}.mp4",
            })

    # videos/README.md: shown by GitHub when the videos folder is opened
    (videos_dir / "README.md").write_text(
        "# Videos\n\n"
        "The videos are hosted on Google Drive, not in this repository.\n\n"
        f"📁 **[Open all {len(tuples) * N_RUNS} videos on Google Drive]"
        f"({DRIVE_LINK})**\n\n"
        "The Drive folder has the same layout as this folder: "
        "`tuple_XX_ka{a}_kg{g}/run_1.mp4` to "
        f"`run_{N_RUNS}.mp4`.\n"
        "Each `tuple_XX_ka{a}_kg{g}` folder here holds only its "
        "`params.json`.\n\n"
        "See the main [README](../README.md) for the tuple-to-parameter "
        "lookup table.\n"
    )

    # Manifest CSV (handy for loading with pandas later)
    with open(ROOT / "manifest.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(manifest_rows[0].keys()))
        writer.writeheader()
        writer.writerows(manifest_rows)

    # README with parameter table
    lines = [
        "# Simulation Videos",
        "",
        f"{len(tuples)} parameter tuples x {N_RUNS} runs = "
        f"{len(tuples) * N_RUNS} videos.",
        "",
        "Parameters: alpha1 = ka+0.5, alpha2 = ka+0.2, "
        "gamma11 = kg+0.2, gamma12 = kg+0.5, gamma22 = kg+0.8, "
        "with ka, kg in {0,1,2,3,4}.",
        "",
        "| # | ka | kg | a1 | a2 | g11 | g12 | g22 | Folder |",
        "|---|----|----|----|----|-----|-----|-----|--------|",
    ]
    for t in tuples:
        p = t["params"]
        lines.append(
            f"| {t['id']} | {t['k_alpha']} | {t['k_gamma']} | {p['alpha1']} | "
            f"{p['alpha2']} | {p['gamma11']} | {p['gamma12']} | {p['gamma22']} "
            f"| [`{t['name']}`](videos/{t['name']}) |"
        )
    lines += ["", "Videos are named `run_1.mp4`, `run_2.mp4`, `run_3.mp4` "
              "inside each tuple folder.", ""]
    (ROOT / "README.md").write_text("\n".join(lines))

    # Git LFS for videos (GitHub rejects files > 100 MB)
    (ROOT / ".gitattributes").write_text(
        "*.mp4 filter=lfs diff=lfs merge=lfs -text\n"
        "*.mov filter=lfs diff=lfs merge=lfs -text\n"
        "*.avi filter=lfs diff=lfs merge=lfs -text\n"
    )
    (ROOT / ".gitignore").write_text(
        ".ipynb_checkpoints/\n__pycache__/\n.DS_Store\n"
    )
    print(f"Created {ROOT}/ with {len(tuples)} tuple folders.")


if __name__ == "__main__":
    main()
