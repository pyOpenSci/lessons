import json
from pathlib import Path

import pandas as pd


def load_clean_json(file_path, columns_to_keep):
    """
    Load JSON data from a file. Drop unnecessary columns and normalize
    to DataFrame.

    Parameters
    ----------
    file_path : Path
        Path to the JSON file.
    columns_to_keep : list
        List of columns to keep in the DataFrame.

    Returns
    -------
    dict
        Loaded JSON data.
    """

    with file_path.open("r") as json_file:
        json_data = json.load(json_file)
    normalized_data = pd.json_normalize(json_data)

    return normalized_data.filter(items=columns_to_keep)


def format_date(date_parts: list) -> str:
    """
    Format date parts into a string.

    Parameters
    ----------
    date_parts : list
        List containing year, month, and day.

    Returns
    -------
    str
        Formatted date string.
    """
    return f"{date_parts[0]}-{date_parts[1]:02d}-{date_parts[2]:02d}"


def clean_title(value):
    """A function that removes a value contained in a list."""
    return value[0]


def process_published_date(date_parts):
    """Parse a date provided as a list of values into a proper date format.

    Parameters
    ----------
    date_parts : str or int
        The elements of a date provided as a list from CrossRef

    Returns
    -------
    pd.datetime
        A date formatted as a pd.datetime object.
    """

    date_str = (
        f"{date_parts[0][0]}-{date_parts[0][1]:02d}-{date_parts[0][2]:02d}"
    )
    return pd.to_datetime(date_str, format="%Y-%m-%d")


columns_to_keep = [
    "publisher",
    "DOI",
    "type",
    "author",
    "is-referenced-by-count",
    "title",
    "published.date-parts",
]

current_dir = Path(__file__).parent
data_dir = current_dir / "data"

all_papers_list = []
for json_file in data_dir.glob("*.json"):
    papers_df = load_clean_json(json_file, columns_to_keep)

    papers_df["title"] = papers_df["title"].apply(clean_title)
    papers_df["published_date"] = papers_df["published.date-parts"].apply(
        process_published_date
    )

    all_papers_list.append(papers_df)

all_papers_df = pd.concat(all_papers_list, axis=0, ignore_index=True)

print("Final shape of combined DataFrame:", all_papers_df.shape)
