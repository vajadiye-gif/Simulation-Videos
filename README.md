# Simulation Videos

Screen recordings of simulations for 25 parameter tuples, with 3 independent runs per tuple (75 videos in total). The aim is a qualitative comparison of behaviour across parameter sets and across runs.

## Download the videos

📁 **[Open all 75 videos on Google Drive](https://drive.google.com/drive/folders/1WyvIvhv-h80lf_WhIfWipEAfWuK6Ef2r?usp=sharing)**

The Drive folder uses the same layout as this repository (`tuple_XX_ka{a}_kg{g}/run_N.mp4`), so the paths in `manifest.csv` match.

## How to tell which tuple is which

**Folder name.** Each folder is named `tuple_XX_ka{a}_kg{g}`:

- `XX` is the tuple number (01 to 25).
- `ka` sets the alpha values: alpha1 = ka + 0.5, alpha2 = ka + 0.2.
- `kg` sets the gamma values: gamma11 = kg + 0.2, gamma12 = kg + 0.5, gamma22 = kg + 0.8.

**Worked example.** `tuple_08_ka1_kg2/run_2.mp4` is run 2 of tuple 8:
ka = 1 gives alpha1 = 1.5, alpha2 = 1.2, and kg = 2 gives gamma11 = 2.2, gamma12 = 2.5, gamma22 = 2.8. Its grid is 140x140 because tuple 8 is in the range 6-15.

**Number to (ka, kg).** Tuple number = 5 * ka + kg + 1. To go back, use ka = (n - 1) // 5 and kg = (n - 1) % 5.

**Lookup grid** (rows = ka, columns = kg):

| | kg = 0 | kg = 1 | kg = 2 | kg = 3 | kg = 4 |
|---|---|---|---|---|---|
| **ka = 0** | 1 | 2 | 3 | 4 | 5 |
| **ka = 1** | 6 | 7 | 8 | 9 | 10 |
| **ka = 2** | 11 | 12 | 13 | 14 | 15 |
| **ka = 3** | 16 | 17 | 18 | 19 | 20 |
| **ka = 4** | 21 | 22 | 23 | 24 | 25 |

**Other ways to check.**

- `params.json` inside each folder lists the exact values for that tuple.
- The full parameter table below and `manifest.csv` list every tuple and video.
- The parameters are also shown in the plot title of each video.

## Simulation settings

| Setting | Value |
|---|---|
| Monte Carlo steps per run | 200,000 |
| Frame interval | 1 frame every 400 MC steps |
| Frames per video | 500 |
| Grid size, tuples 6-15 | 140 x 140 |
| Grid size, all other tuples (1-5, 16-25) | 120 x 120 |
| Runs per tuple | 3 |
| Random seed | not fixed; each run is an independent realisation |

**Why two grid sizes:** in tuples 6-15 (ka = 1 and ka = 2) some cells reached the domain boundary on the 120 x 120 grid, so those tuples were rerun on a larger 140 x 140 grid. Keep this in mind when comparing videos across the two groups, since the domain size differs.

## Parameters

For each tuple:

- alpha1 = ka + 0.5
- alpha2 = ka + 0.2
- gamma11 = kg + 0.2
- gamma12 = kg + 0.5
- gamma22 = kg + 0.8

with ka, kg in {0, 1, 2, 3, 4}. Tuple number = 5 * ka + kg + 1.

| # | ka | kg | alpha1 | alpha2 | gamma11 | gamma12 | gamma22 | Grid | Folder |
|---|----|----|--------|--------|---------|---------|---------|------|--------|
| 1 | 0 | 0 | 0.5 | 0.2 | 0.2 | 0.5 | 0.8 | 120x120 | [`tuple_01_ka0_kg0`](videos/tuple_01_ka0_kg0) |
| 2 | 0 | 1 | 0.5 | 0.2 | 1.2 | 1.5 | 1.8 | 120x120 | [`tuple_02_ka0_kg1`](videos/tuple_02_ka0_kg1) |
| 3 | 0 | 2 | 0.5 | 0.2 | 2.2 | 2.5 | 2.8 | 120x120 | [`tuple_03_ka0_kg2`](videos/tuple_03_ka0_kg2) |
| 4 | 0 | 3 | 0.5 | 0.2 | 3.2 | 3.5 | 3.8 | 120x120 | [`tuple_04_ka0_kg3`](videos/tuple_04_ka0_kg3) |
| 5 | 0 | 4 | 0.5 | 0.2 | 4.2 | 4.5 | 4.8 | 120x120 | [`tuple_05_ka0_kg4`](videos/tuple_05_ka0_kg4) |
| 6 | 1 | 0 | 1.5 | 1.2 | 0.2 | 0.5 | 0.8 | 140x140 | [`tuple_06_ka1_kg0`](videos/tuple_06_ka1_kg0) |
| 7 | 1 | 1 | 1.5 | 1.2 | 1.2 | 1.5 | 1.8 | 140x140 | [`tuple_07_ka1_kg1`](videos/tuple_07_ka1_kg1) |
| 8 | 1 | 2 | 1.5 | 1.2 | 2.2 | 2.5 | 2.8 | 140x140 | [`tuple_08_ka1_kg2`](videos/tuple_08_ka1_kg2) |
| 9 | 1 | 3 | 1.5 | 1.2 | 3.2 | 3.5 | 3.8 | 140x140 | [`tuple_09_ka1_kg3`](videos/tuple_09_ka1_kg3) |
| 10 | 1 | 4 | 1.5 | 1.2 | 4.2 | 4.5 | 4.8 | 140x140 | [`tuple_10_ka1_kg4`](videos/tuple_10_ka1_kg4) |
| 11 | 2 | 0 | 2.5 | 2.2 | 0.2 | 0.5 | 0.8 | 140x140 | [`tuple_11_ka2_kg0`](videos/tuple_11_ka2_kg0) |
| 12 | 2 | 1 | 2.5 | 2.2 | 1.2 | 1.5 | 1.8 | 140x140 | [`tuple_12_ka2_kg1`](videos/tuple_12_ka2_kg1) |
| 13 | 2 | 2 | 2.5 | 2.2 | 2.2 | 2.5 | 2.8 | 140x140 | [`tuple_13_ka2_kg2`](videos/tuple_13_ka2_kg2) |
| 14 | 2 | 3 | 2.5 | 2.2 | 3.2 | 3.5 | 3.8 | 140x140 | [`tuple_14_ka2_kg3`](videos/tuple_14_ka2_kg3) |
| 15 | 2 | 4 | 2.5 | 2.2 | 4.2 | 4.5 | 4.8 | 140x140 | [`tuple_15_ka2_kg4`](videos/tuple_15_ka2_kg4) |
| 16 | 3 | 0 | 3.5 | 3.2 | 0.2 | 0.5 | 0.8 | 120x120 | [`tuple_16_ka3_kg0`](videos/tuple_16_ka3_kg0) |
| 17 | 3 | 1 | 3.5 | 3.2 | 1.2 | 1.5 | 1.8 | 120x120 | [`tuple_17_ka3_kg1`](videos/tuple_17_ka3_kg1) |
| 18 | 3 | 2 | 3.5 | 3.2 | 2.2 | 2.5 | 2.8 | 120x120 | [`tuple_18_ka3_kg2`](videos/tuple_18_ka3_kg2) |
| 19 | 3 | 3 | 3.5 | 3.2 | 3.2 | 3.5 | 3.8 | 120x120 | [`tuple_19_ka3_kg3`](videos/tuple_19_ka3_kg3) |
| 20 | 3 | 4 | 3.5 | 3.2 | 4.2 | 4.5 | 4.8 | 120x120 | [`tuple_20_ka3_kg4`](videos/tuple_20_ka3_kg4) |
| 21 | 4 | 0 | 4.5 | 4.2 | 0.2 | 0.5 | 0.8 | 120x120 | [`tuple_21_ka4_kg0`](videos/tuple_21_ka4_kg0) |
| 22 | 4 | 1 | 4.5 | 4.2 | 1.2 | 1.5 | 1.8 | 120x120 | [`tuple_22_ka4_kg1`](videos/tuple_22_ka4_kg1) |
| 23 | 4 | 2 | 4.5 | 4.2 | 2.2 | 2.5 | 2.8 | 120x120 | [`tuple_23_ka4_kg2`](videos/tuple_23_ka4_kg2) |
| 24 | 4 | 3 | 4.5 | 4.2 | 3.2 | 3.5 | 3.8 | 120x120 | [`tuple_24_ka4_kg3`](videos/tuple_24_ka4_kg3) |
| 25 | 4 | 4 | 4.5 | 4.2 | 4.2 | 4.5 | 4.8 | 120x120 | [`tuple_25_ka4_kg4`](videos/tuple_25_ka4_kg4) |

## Repository layout

The videos are hosted on Google Drive (see the link at the top), not in this repository. The repo holds only the code, the `params.json` files and `manifest.csv`.

```
videos/
  README.md          # Drive link for the videos
  tuple_XX_ka{a}_kg{g}/
    params.json      # exact parameter values for this tuple
    run_1.mp4        # on Drive only
    run_2.mp4        # on Drive only
    run_3.mp4        # on Drive only
manifest.csv         # one row per video: tuple, parameters, run, path
setup_repo.py        # regenerates the folder skeleton
```

## Looking up a video

```python
import pandas as pd

df = pd.read_csv("manifest.csv")

# All videos for ka = 1, kg = 2
print(df[(df["k_alpha"] == 1) & (df["k_gamma"] == 2)]["video_path"].tolist())
```

The paths in `manifest.csv` are relative to the Drive folder root. Each video also shows its parameters in the plot title, so a clip stays identifiable if it is moved or renamed.
