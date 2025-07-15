# Dataset Analysis Scripts

This repository provides three approaches for summarizing and analyzing tabular datasets (CSV):
- **Pure Python** (no external dependencies)
- **Pandas** (industry standard for data analysis)
- **Polars** (fast, modern alternative to pandas)

## Directory Structure
```
2023 fb posts dataset/
    pandas_stats.py
    polar_stats.py
    pure_python_stats.py
    2024_fb_posts_president_scored_anon.csv
2024 fb ads dataset/
    pandas_stats.py
    polar_stats.py
    pure_python_stats.py
    2024_fb_ads_president_scored_anon.csv
2024 twitter posts dataset/
    pandas_stats.py
    polar_stats.py
    pure_python_stats.py
    2024_tw_posts_president_scored_anon.csv
```

## Usage
Run the desired script in the appropriate folder. Example:

```sh
cd '2024 fb ads dataset'
python3 pure_python_stats.py
python3 pandas_stats.py
python3 polar_stats.py
```

Each script prints, for each column and for the dataset overall:
- Count
- Mean (for numeric fields)
- Minimum and maximum values
- Standard deviation
- For non-numeric fields: unique value counts and most frequent values

Grouped analysis is performed by:
- `page_id` for Facebook ads
- `Facebook_Id` for Facebook posts
- `source` for Twitter posts

## Requirements
See `requirements.txt` for dependencies. Pure Python script requires no installation. For pandas and polars, install dependencies:

```sh
pip install -r requirements.txt
```

## Data Files
**No dataset files are committed to this repository, but you can download them from here: [Google Drive Link](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing).**

## .gitignore
The `.gitignore` file excludes all CSV and dataset files from version control.
