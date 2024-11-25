import requests
import pandas as pd
import concurrent.futures

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

_scrape_all_sources_called = False


def fetch_data(url: str, col_data: list) -> pd.DataFrame:
    """
    Scrape data from website. In col_data, Status 0.0 means data is up to date,
        Status 1.0 means data has not been finalized
    Inputs:
        url: url to website to scrape from
        col_data: list of names for each column of data
    Output:
        return df: a DataFrame from url containing col_data or None for error request
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request fails

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

        # Convert data to YYYY-MM-DD
        df = pd.DataFrame(data)

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
    Output:
        results: dictionary of scraped data with keys set to columns
    """

    global _scrape_all_sources_called

    results = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url = {
            executor.submit(fetch_data, url, column_name): url
            for url, column_name in zip(sources, columns)
        }

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                results[url] = data
            except Exception as e:
                print(f"Error processing {url}: {e}")

    _scrape_all_sources_called = True

    return results


def update_cols(old_dict: dict) -> dict:
    """
    Replace url keys with more readable keys corresponding to url data. Must call scrape_all_sources() before calling update_cols()
    Input:
        old_dict: dictionary containing scraped data with url keys
    Output:
        old_dict: new dictionary containing readable, updated key names
    """

    if not _scrape_all_sources_called:
        raise RuntimeError(
            "'scrape_all_sources()' must be called before using 'update_cols()'"
        )

    old_dict["Yearly SSN"] = old_dict.pop(
        "https://www.sidc.be/SILSO/DATA/SN_y_tot_V2.0.txt"
    )
    old_dict["Monthly SSN"] = old_dict.pop(
        "https://www.sidc.be/SILSO/DATA/SN_m_tot_V2.0.txt"
    )
    old_dict["Smoothed SSN"] = old_dict.pop(
        "https://www.sidc.be/SILSO/DATA/SN_ms_tot_V2.0.txt"
    )
    old_dict["Daily SSN"] = old_dict.pop(
        "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"
    )

    return old_dict
