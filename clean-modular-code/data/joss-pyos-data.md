---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

A notebook to process the data

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import os
import requests
import time
import json
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Crossref API base URL
base_url = "https://api.crossref.org/works"

# Define the start date as a variable
start_date = "2019-05-01"
end_date = "2022-05-01"


# Parameters for the API request
params = {
    'filter': f'type:journal-article,container-title:Journal of Open Source Software,from-pub-date:{start_date},until-pub-date:{end_date}',
    'rows': 50  # 50 rows per request to match the rate limit / second
}


headers = {
    'User-Agent': 'pyOSworkshop/1.0 (mailto:leah@pyopensci.org)',
}

# Initialize variables
all_publications = []
offset = 0
rate_limit = 50  # 50 requests per second
rate_interval = 1  # 1 second interval for the rate limit

# Fetch publications using pagination
while True:
    # Update the offset parameter for pagination
    params['offset'] = offset
    response = requests.get(base_url, params=params, headers=headers)
    publications = response.json()
    all_publications.extend(publications['message']['items'])

    # If there are no more publications to retrieve, stop the loop
    if len(publications['message']['items']) == 0:
        break

    # Update the offset to fetch the next page
    offset += 50  
    
    # Rate limit: pause for 1 second after each request
    time.sleep(rate_interval)

# Create a dictionary that mimics Habanero output
joss_pubs = {
    "status": "ok",
    "message-type": "work-list",
    "message-version": "1.0.0",
    "message": {
        "total-results": len(all_publications),
        "items": all_publications
    }
}

with open("joss_publications.json", "w") as f:
    json.dump(joss_pubs, f, indent=2)

# Print the total number of publications retrieved
print(f"Total Publications Retrieved: {len(all_publications)}")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
type(joss_pubs)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Export data to json for teaching - 17mb
with open(os.path.join('data', 'joss-publications.json'), 'w') as f:
    json.dump(joss_pubs, f)

print(f"Total JOSS publications: {total_results}")
joss_pubs.keys()
```

## Workflow to get data by year

```{code-cell} ipython3
import requests
import json
import time

# Crossref API base URL
base_url = "https://api.crossref.org/works"

# Define the date ranges as a list of tuples
date_ranges = [
    ("2019-01-01", "2019-12-31"),
    ("2020-01-01", "2020-12-31"),
    ("2021-01-01", "2021-12-31"),
    ("2022-01-01", "2022-12-31"),
    ("2023-01-01", "2023-12-31"),
    ("2024-01-01", "2024-12-31")
    
]

# Headers for the API request
headers = {
    'User-Agent': 'pyOSworkshop/1.0 (mailto:leah@pyopensci.org)',
}

# Initialize variables
rate_limit = 50  # 50 requests per second
rate_interval = 1  # 1 second interval for the rate limit

# Function to fetch publications for a given date range
def fetch_publications(start_date, end_date):
    all_publications = []
    offset = 0

    # Parameters for the API request
    params = {
        'filter': f'type:journal-article,container-title:Journal of Open Source Software,from-pub-date:{start_date},until-pub-date:{end_date}',
        'rows': 50  # 50 rows per request to match the rate limit / second
    }

    # Fetch publications using pagination
    while True:
        # Update the offset parameter for pagination
        params['offset'] = offset
        response = requests.get(base_url, params=params, headers=headers)
        publications = response.json()
        all_publications.extend(publications['message']['items'])

        # If there are no more publications to retrieve, stop the loop
        if len(publications['message']['items']) == 0:
            break

        # Update the offset to fetch the next page
        offset += 50  

        # Rate limit: pause for 1 second after each request
        time.sleep(rate_interval)

    return all_publications

# Loop through each date range and fetch publications
for start_date, end_date in date_ranges:
    joss_pubs = fetch_publications(start_date, end_date)
    year = start_date.split('-')[0]

    # Save the results to a file named according to the date range
    file_name = f"{year}-joss-publications.json"
    json_path = os.path.join("data", file_name)
    with open(json_path, "w") as f:
        json.dump(joss_pubs, f, indent=2)

    # Print the total number of publications retrieved for this date range
    print(f"Total Publications Retrieved for {start_date} to {end_date}: {len(joss_pubs)}")

```

```{code-cell} ipython3
joss_pubs[0]
```

```{code-cell} ipython3
file_name
import os
os.getcwd()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [hide-input]
---
#This doesn't properly handle pagination and rate limits
# cr = Crossref(mailto="leah@pyopensci.org")  # polite pool

# # Initialize variables
# total_results = 2412  # Example total count (replace with actual value from API response)
# rows_per_page = 100  # Number of items per request (Crossref's maximum allowed is usually 100)
# all_publications = []

# # Loop to fetch all results using pagination
# for offset in range(0, total_results, rows_per_page):
#     publications = cr.works(filter={'type': 'journal-article', 
#                                     'container-title': 'Journal of Open Source Software',
#                                     'from-pub-date': '2019-05-01'},                           
#                                     offset=offset, rows=rows_per_page)
    
#     # Append the items from each page to the list
#     all_publications.extend(publications['message']['items'])

# # Check the total number of publications retrieved
# print(f"Total JOSS publications retrieved: {len(all_publications)}")
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Data structure

* facets: Empty, in this case, could represent filtering or categorization data.
* total-results: The total number of results (in this case, 2412).
* items: A list containing metadata about each article. Each entry in the items list represents an individual article with its associated metadata.

### Citation data structure

Within items you have each publication which follows this structure


- **indexed**: Contains information about when the article was indexed by the service.
  - **date-parts**: The date the article was indexed.
  - **date-time**: The full date-time the article was indexed.
  - **timestamp**: A UNIX timestamp indicating when the article was indexed.
- **reference-count**: The number of references in the article.
- **publisher**: The name of the publisher.
- **issue**: The issue number in which the article was published.
- **license**: Contains license information for the article.
  - **start**: The start date of the license.
  - **URL**: The URL where the license can be found.
- **content-domain**: Indicates any domain restrictions for the content (none here).
- **DOI**: The article’s DOI (Digital Object Identifier).
- **type**: The type of article (journal-article in this case).
- **created**: Contains the creation date for the metadata entry (when it was first added to the system).
- **page**: Page number or range where the article appears.
- **source**: Source of the metadata (Crossref in this case).
- **is-referenced-by-count**: The number of times this article has been referenced by other works.
- **title**: A list containing the title of the article.
- **prefix**: The DOI prefix, used to identify the publisher.
- **author**: A list of dictionaries, each representing an author of the article. Each author has:
  - **given**: The given name of the author.
  - **family**: The family name (surname) of the author.
  - **ORCID**: The author’s ORCID ID, if available.
- **reference**: A list of references cited by the article, including DOIs and unstructured references.
- **container-title**: The name of the journal in which the article was published.
- **link**: A list of dictionaries, each containing URLs to the article.
- **deposited**: Metadata about when the article’s metadata was deposited, including:
  - **date-parts**: Date of deposition.
  - **timestamp**: UNIX timestamp for the deposition.
- **score**: A relevance score for the article (often used in search results).
- **issued**: The date when the article was published.
- **journal-issue**: Information about the issue in which the article was published.
  - **issue**: The issue number.
  - **published-online**: The date when the issue was published online.
- **alternative-id**: Alternative identifiers for the article.
- **URL**: The article’s URL (usually the DOI link).
- **relation**: Information about related works, including reviews and references.
- **ISSN**: The ISSN (International Standard Serial Number) for the journal.
- **published**: Another key that captures the publication date of the article.

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Load the CSV file and return a list of package names
accepted_packages = pd.read_csv(os.path.join('data', 'pyos-joss-accepted-packages.csv'))

# Extract the names from the CSV
package_names = accepted_packages["package-name"].to_list()
package_names
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
pyos_count = 0
for i, pub in enumerate(all_publications):
    title = pub["title"][0].lower().split(":")[0].lower()
    for name in package_names:
        if name.lower() in title:
            pyos_count += 1
            print(f"Title: {title}")
            print(f"pyOS Name: {name}")

print(f"Total pubs processed: {i}")
print(pyos_count)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```
