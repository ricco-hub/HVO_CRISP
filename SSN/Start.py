import requests
import os
import datetime
import csv

SSN_ALL = r"C:\Users\ricco\OneDrive\Desktop\HVO_CRISP\SSN\SSN_ALL.txt"
CACHE_FILE = "SSN_ALL.csv"
URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


current_time = datetime.datetime.now()
cache_expiry = current_time.day < 2
print(cache_expiry)


def is_cache_valid() -> bool:
    # Check if the cache file exists and is within the expiry time
    if os.path.exists(CACHE_FILE):
        return cache_expiry
    return False


def load_from_cache():
    # Load cached data from CSV file
    data = []
    with open(CACHE_FILE, mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def save_to_cache(data):
    # Save new data to CSV cache
    with open(CACHE_FILE, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        for row in data:
            if not row[4] == "-1" or row[4] == "-1.0":
                writer.writerow(row)
            else:
                continue


def fetch_data():
    # Check if cache is valid
    if is_cache_valid():
        print("Loading data from cache.")
        return load_from_cache()

    # Fetch new data from the URL
    print("Fetching data from the web.")
    response = requests.get(URL, allow_redirects=True)
    response.raise_for_status()  # Raise an error for bad status codes

    # Process the data (split into rows, etc.) assuming each line is a new data row
    data = [line.split() for line in response.text.splitlines()]

    # Cache the data in a CSV file
    save_to_cache(data)
    return data


# Usage example
if __name__ == "__main__":
    col_names = [
        "year",
        "month",
        "day",
        "year_dec",
        "AR",
        "mag",
        "SSN",
        "star",
    ]  # just guessing, need to ask David
    data = fetch_data()
    print(data)


#################################################################################################################
# # open(r"C:\Users\ricco\OneDrive\Desktop\HVO_CRISP\SSN\SSN_Hist.txt", "w").close() # creating or clearing file every time Start.py is called
# # also only used to open and close file, not sure if this is used elsewhere in the VM
# current_time = datetime.datetime.now()

# if current_time.day != 1 and current_time.day != 2: # what happens when it's the first or second of the month? Why only 1st & 2nd?
#     url = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"
#     r = requests.get(url, allow_redirects=True)
#     # scarico storico
#     open(SSN_ALL, "wb").write(r.content) # writes everyday other than 1st or 2nd of month

#     line = tuple(open(time.strftime(SSN_ALL), "r"))

#     # dallo storico elimino le righe in cui non si hanno dati mancanti che inSILSO vengono indicati con '-1'
#     with open(time.strftime(SSN_ALL), "w") as file:
#         for j in range(len(line)):
#             sline = line[j].split()
#             if not sline[4] == "-1" or sline[4] == "-1.0":
#                 file.write(line[j])
