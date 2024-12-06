import requests
import pandas as pd
import concurrent.futures
import warnings
import os

from io import StringIO
from concurrent.futures import ThreadPoolExecutor

URLS = [
    "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt",
    "https://www.sidc.be/SILSO/DATA/SN_m_tot_V2.0.txt",
    "https://www.sidc.be/SILSO/DATA/SN_ms_tot_V2.0.txt",
    "https://www.sidc.be/SILSO/DATA/SN_y_tot_V2.0.txt",
]

COL_DATA_DAILY = [
    "year",
    "month",
    "day",
    "decimal year",
    "SNvalue",
    "SNerror",
    "Nb observations",
    "Status",
]

COL_DATA_MONTHLY = [
    "year",
    "month",
    "decimal year",
    "SNvalue",
    "SNerror",
    "Nb observations",
    "Status",
]

COL_DATA_SMOOTH = COL_DATA_MONTHLY

COL_DATA_YEARLY = [
    "mid year",
    "SNvalue",
    "SNerror",
    "Nb observations",
    "Status",
]

COLUMNS = [COL_DATA_DAILY, COL_DATA_MONTHLY, COL_DATA_SMOOTH, COL_DATA_YEARLY]


def fetch_data(url: str, col_data: list, save_dir: str = "test") -> pd.DataFrame:
    """
    Scrape data from website and save in pickle file.
        In col_data, Status 0.0 means data is up to date,
        Status 1.0 means data has not been finalized

        save_dir: name of directory to save pickle files
    Inputs:
        url: url to website to scrape from
        col_data: list of names for each column of data
    Output:
        return df: a DataFrame from url containing col_data or None for error request
    """

    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an error if the request fails
        warnings.filterwarnings("ignore", message="Unverified HTTPS request")

        # Convert the txt data to a DataFrame
        data = pd.read_csv(
            StringIO(response.text),
            header=None,
            names=col_data,
            sep=r"\s+",
            dtype={"Status": str},
            low_memory=False,
        )

        # Remove asterisks from Status and convert to numeric
        data["Status"] = pd.to_numeric(
            data["Status"].str.replace("*", "1"), errors="coerce"
        )
        # Replace NaN with 0.0
        data["Status"] = data["Status"].fillna(0)
        # Only include SSN values that are not -1
        data = data[~data["SNvalue"].isin([-1, -1.0])]

        # Replace -1 in SNerror with 0
        data["SNerror"] = data["SNerror"].replace(-1, 0)

        # Convert data to YYYY-MM-DD
        df = pd.DataFrame(data)

        # Save in pickle file
        os.makedirs(save_dir, exist_ok=True)
        filename = os.path.join(save_dir, url.split("/")[-1].replace(".txt", ".pkl"))
        df.to_pickle(filename)

        return df
    except requests.RequestException as e:
        print(f"Failed to scrape {url}: {e}")
        return None


def scrape_all_sources(sources: list, columns: list):
    """
    Implement I/O bound parallel computing for list of sources sources with column data columns
    Inputs:
        sources: generic list of urls to scrape from
        columns: generic list of column data names
    """

    with ThreadPoolExecutor(max_workers=8) as executor:
        {
            executor.submit(fetch_data, url, column_name): url
            for url, column_name in zip(sources, columns)
        }


if __name__ == "__main__":
    scrape_all_sources(URLS, COLUMNS)
