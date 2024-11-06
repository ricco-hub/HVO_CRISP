import requests
import os
import datetime
import csv

CACHE_FILE = "SSN_ALL.csv"
URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


current_time = datetime.datetime.now()
cache_expiry = current_time.day != 1 and current_time.day != 2


def is_cache_valid() -> bool:
    # Check if the cache file exists and is within the expiry time
    if os.path.exists(CACHE_FILE):
        return cache_expiry
    return False


def save_to_cache(data):
    # Save new data to CSV cache
    with open(CACHE_FILE, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # remove -1 in SNvalue column
        for row in data:
            if row[4] != "-1":
                writer.writerow(row)
            else:
                continue


def fetch_data():
    # Check if cache is valid
    if is_cache_valid():
        # Fetch new data from the URL
        response = requests.get(URL, allow_redirects=True)
        response.raise_for_status()  # Raise an error for bad status codes

        # Process the data (split into rows, etc.) assuming each line is a new data row
        data = [line.split() for line in response.text.splitlines()]

        # Cache the data in a CSV file
        save_to_cache(data)


if __name__ == "__main__":
    column_data = [
        "year",
        "month",
        "day",
        "decimal year",
        "SNvalue",
        "SNerror",
        "Nb observations",
    ]
    fetch_data()
