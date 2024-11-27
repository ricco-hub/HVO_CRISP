import pandas as pd

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, DateRangePicker, Button, CustomJS
from bokeh.layouts import column, row
from bokeh.io import curdoc
from datetime import datetime
from callbacks import update_hover_data, reset_data
from functools import partial
from get_solar_data import *

URL = "http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt"


df = fetch_data(URL, COL_DATA_DAILY)
# Using pd.to_datetime to create a datetime object
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

# Attach Callback to the DateRangeSlider
date_range_picker.on_change(
    "value",
    partial(update_hover_data, date_range=date_range_picker, data=df, source=source),
)

# Reset button
reset_button = Button(label="Reset Data", button_type="primary")

reset_button.on_click(
    partial(reset_data, original_data=df, date_picker=date_range_picker)
)

# Download button
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT data", button_type="success")


# CustomJS for downloading data
txt_code = """
function tableToText(source) {
    const columns = Object.keys(source.data);
    const rows = source.get_length();
    const text = [];

    // Data rows
    for (let i = 0; i < rows; i++) {
        const row = columns.map(column => source.data[column][i]);
        text.push(row.join('\\t')); // Tab-separated values
    }

    return text.join('\\n');
}

// Convert data to text format
const text = tableToText(source);

// Create a Blob with text data and trigger a download
const blob = new Blob([text], { type: 'text/plain' });
const url = URL.createObjectURL(blob);

const a = document.createElement('a');
a.href = url;
a.download = 'ssn_data.txt';
a.click();
URL.revokeObjectURL(url);
"""

csv_code = """
function tableToCSV(source) {
    const columns = Object.keys(source.data);
    const rows = source.get_length();
    const csv = [];

    // Header row
    csv.push(columns.join(','));

    // Data rows
    for (let i = 0; i < rows; i++) {
        const row = columns.map(column => source.data[column][i]);
        csv.push(row.join(','));
    }

    return csv.join('\\n');
}

// Convert data to CSV format
const csv = tableToCSV(source);

// Create a Blob with CSV data and trigger a download
const blob = new Blob([csv], { type: 'text/csv' });
const url = URL.createObjectURL(blob);

const a = document.createElement('a');
a.href = url;
a.download = 'ssn_data.csv';
a.click();
URL.revokeObjectURL(url);
"""

download_csv_button.js_on_click(CustomJS(args=dict(source=source), code=csv_code))
download_txt_button.js_on_click(CustomJS(args=dict(source=source), code=txt_code))

layout = column(
    row(date_range_picker, reset_button),
    plot,
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)
curdoc().add_root(layout)
