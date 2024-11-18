import requests
import pandas as pd

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, DateRangePicker
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.embed import server_document
from io import StringIO
from datetime import datetime

URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


# Function to scrape data from a remote txt file
def fetch_data():
    response = requests.get(URL)
    response.raise_for_status()  # Raise an error if the request fails

    # Convert the CSV data to a DataFrame
    column_data = [
        "year",
        "month",
        "day",
        "decimal year",
        "SNvalue",
        "SNerror",
        "Nb observations",
        "Status",
    ]

    data = pd.read_csv(
        StringIO(response.text),
        header=None,
        names=column_data,
        sep=r"\s+",
        dtype={"Status": str},
        low_memory=False,
    )
    # Remove asterisks from Status and convert to numeric
    data["Status"] = pd.to_numeric(
        data["Status"].str.replace("*", "1"), errors="coerce"
    )
    data["Status"] = data["Status"].fillna(0)
    data = data[~data["SNvalue"].isin([-1, -1.0])]
    return data


# Fetch the data
data = fetch_data()

# Convert data to YYYY-MM-DD
df = pd.DataFrame(data)

# # Using pd.to_datetime to create a datetime object
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

source = ColumnDataSource(
    data=dict(
        dec_year=df["decimal year"],
        sn_value=df["SNvalue"],
        date=df["date"],
        year=df["year"],
    )
)

# Create a scatter plot
plot = figure(
    title="Sunspot Number",
    x_axis_label="Time (decimal year)",
    y_axis_label="Sunspot Number",
    width=1000,
    height=700,
    sizing_mode="scale_both",
)
plot.scatter(
    "dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.5
)  # make dec_year more human readable

# create hover tool
renderer = plot.circle(
    "dec_year", "sn_value", source=source, size=8, color="navy", alpha=0.0
)

hover = HoverTool(
    tooltips=[("Year", "@dec_year"), ("SSN", "@sn_value")], renderers=[renderer]
)  # dec_year rounding

plot.add_tools(hover)

# Create DateRangeSlider
min_date = datetime(1818, 1, 1).date()
max_date = max(df["date"]).date()
date_range_picker = DateRangePicker(
    title="Select data range manually. Double click to select a date.",
    value=(min_date, max_date),
    min_date=min_date,
    max_date=max_date,
)

# Define python callback
def update_data(attr, old, new):
    """
    Python callback to update data everytime user picks new data range
    """

    # Get the date range selected in the DateRangeSlider
    start_date, end_date = date_range_picker.value

    # convert to datetime.date
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    # convert to datetime.datetime
    start_date = datetime.combine(start_date, datetime.min.time())
    end_date = datetime.combine(end_date, datetime.max.time())

    # Filter the data based on the selected date range
    filtered_data = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    # Update the data source with filtered data
    source.data = {
        "dec_year": filtered_data["decimal year"],
        "sn_value": filtered_data["SNvalue"],
    }


# Attach Callback to the DateRangeSlider
date_range_picker.on_change("value", update_data)

layout = column(date_range_picker, plot, sizing_mode="stretch_both")
curdoc().add_root(layout)

# Get tag to include in HTML file
# script = server_document()
# print(script)
