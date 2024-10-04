"""Solution - part 1 

Important elements
* 
* 
"""

# This is what the code could look like after part 1.
import json
from pathlib import Path

import pandas as pd

# Use pathlib to ensure your code runs on other machines (assuming relative paths)
file_path = Path("data") / "part-1-data.json"

# Load JSON data
with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

# Normalize JSON data into a flat table
normalized_data = pd.json_normalize(json_data)

# Define columns to keep
columns_to_keep = [
    "publisher",
    "DOI",
    "type",
    "author",
    "is-referenced-by-count",
    "title",
    "published.date-parts",
]

# Filter the DataFrame by the desired columns
papers_df_1 = normalized_data.filter(items=columns_to_keep)

# Iterate through each row and extract date and title
for index, row in papers_df_1.iterrows():
    date_parts = row["published.date-parts"][0]
    papers_df_1.at[index, "title"] = papers_df_1.at[index, "title"][0]

    formatted_date = f"{date_parts[0]}-{date_parts[1]:02d}-{date_parts[2]:02d}"
    published_date = pd.to_datetime(formatted_date, format="%Y-%m-%d")

    papers_df_1.at[index, "published_date"] = published_date

# Drop the original "published.date-parts" column
papers_df_1.drop("published.date-parts", axis=1, inplace=True)

# Print the shape of the first DataFrame
print(papers_df_1.shape)

# Load and process the second JSON data
file_path_b = "data/part-1-datab.json"

with open(file_path_b, "r") as json_file_b:
    json_data_b = json.load(json_file_b)

normalized_data_b = pd.json_normalize(json_data_b)

# Filter the second DataFrame by the same columns
papers_df_2 = normalized_data_b.filter(items=columns_to_keep)

# Iterate through each row and extract date and title for the second DataFrame
for index, row in papers_df_2.iterrows():
    date_parts_b = row["published.date-parts"][0]
    papers_df_2.at[index, "title"] = papers_df_1.at[index, "title"][0]

    formatted_date_b = (
        f"{date_parts_b[0]}-{date_parts_b[1]:02d}-{date_parts_b[2]:02d}"
    )
    published_date_b = pd.to_datetime(formatted_date_b, format="%Y-%m-%d")

    papers_df_2.at[index, "published_date"] = published_date_b

# Drop the original "published.date-parts" column from the second DataFrame
papers_df_2.drop("published.date-parts", axis=1, inplace=True)

# Concatenate the two DataFrames
combined_papers_df = pd.concat([papers_df_1, papers_df_2], axis=0)

# Print the shape of the combined DataFrame
combined_papers_df.shape
