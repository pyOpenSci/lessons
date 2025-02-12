"""Module that supports fetching cross-ref publication data from JOSS 
using the API. 

Returns the data as individual files as follows:

2019-joss-publications.json

Data are stored as a JSON format
Publication data are ingested as a list of dictionaries where each dict represents a single publication. 

"""

import os
import requests
import json
import time

print(os.getcwd())

# Crossref API base URL
base_url = "https://api.crossref.org/works"

# Define the date ranges as a list of tuples
date_ranges = [
    ("2019-01-01", "2019-12-31"),
    # ("2020-01-01", "2020-12-31"),
    # ("2021-01-01", "2021-12-31"),
    # ("2022-01-01", "2022-12-31"),
    # ("2023-01-01", "2023-12-31"),
    # ("2024-01-01", "2024-12-31"),
]

# Headers for the API request
headers = {
    "User-Agent": "pyOSworkshop/1.0 (mailto:leah@pyopensci.org)",
}

# Initialize variables
rate_limit = 50  # 50 requests per second
rate_interval = 1  # 1 second rate limit interval


# Function to fetch publications for a given date range
def fetch_publications(start_date, end_date):
    all_publications = []
    offset = 0

    # Parameters for the API request
    params = {
        "filter": f"type:journal-article,container-title:Journal of Open Source Software,from-pub-date:{start_date},until-pub-date:{end_date}",
        "rows": 50,  # 50 rows per request to match the rate limit / second
    }

    # Fetch publications using pagination
    while True:
        # Update the offset parameter for pagination
        params["offset"] = offset
        response = requests.get(base_url, params=params, headers=headers)
        publications = response.json()
        all_publications.extend(publications["message"]["items"])

        # If there are no more publications to retrieve, stop the loop
        if len(publications["message"]["items"]) == 0:
            break

        # Update the offset to fetch the next page
        offset += 50

        # Rate limit: pause for 1 second after each request
        time.sleep(rate_interval)

    return all_publications


# Loop through each date range and fetch publications
for start_date, end_date in date_ranges:
    joss_pubs = fetch_publications(start_date, end_date)
    year = start_date.split("-")[0]

    # Save the results to a file named according to the date range
    file_name = f"{year}-joss-publications.json"
    json_path = os.path.join("clean-modular-code", "data", file_name)
    with open(json_path, "w") as f:
        json.dump(joss_pubs, f, indent=2)

    # Print the total number of publications retrieved for this date range
    print(
        f"Total Publications Retrieved for {start_date} to {end_date}: {len(joss_pubs)}"
    )
