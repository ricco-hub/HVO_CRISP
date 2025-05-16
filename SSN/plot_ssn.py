import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plots.hvo_plots import *
from bokeh.models import ColumnDataSource, DateRangePicker, Button, CustomJS
from bokeh.layouts import column, row
from bokeh.io import curdoc
from datetime import datetime
from plots.callbacks.callbacks import update_hover_data, reset_data
from functools import partial
from pathlib import Path


df = pd.read_pickle("data/SN_d_tot_V2.0.pkl")
# Using pd.to_datetime to create a datetime object
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

source = ColumnDataSource(data={col: df[col] for col in df.columns})

data = {"Daily SSN": df.copy()}
del data["Daily SSN"]["date"]
source_data = {name: ColumnDataSource(data=series) for name, series in data.items()}

# Create a scatter plot
ssn_plot = HVOPlot("Daily Sunspot Number", "Time (years)", "Sunspot Number", True)
ssn_plot.line_plot(source, "Daily SSN", "decimal_year", "SNvalue")
ssn_plot.add_hover_tool(source, "decimal_year", "SNvalue", "Year", "SSN")
scatter = ssn_plot.line_plot(source, "Daily SSN", "decimal_year", "SNvalue")

# Create DateRangeSlider
min_date = datetime(1818, 1, 1).date()
max_date = max(df["date"]).date()
date_range_picker = DateRangePicker(
    title="Select date range manually. Double click to select a date.",
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
reset_button = Button(label="Reset Plot", button_type="primary")

reset_button.on_click(
    partial(reset_data, original_data=df, date_picker=date_range_picker)
)

# Download button
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT data", button_type="success")

# CustomJS for downloading data
js_callbacks = (
    Path(__file__).parent.parent / "plots" / "callbacks" / "callbacks.js"
).read_text("utf8")

plots = {}
plots["Daily SSN"] = {"scatter": scatter}

download_csv_button.js_on_click(
    CustomJS(
        args=dict(
            source=source_data,
            plots=plots,
            x_range=ssn_plot.get_plot().x_range,
            y_range=ssn_plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;

        // Download data with visible plot names included
        downloadAxes(
          source,
          x_start,
          x_end,
          y_start,
          y_end,
          plots,
          "csv",
          "SSN"
        );
       """,
    )
)

download_txt_button.js_on_click(
    CustomJS(
        args=dict(
            source=source_data,
            plots=plots,
            x_range=ssn_plot.get_plot().x_range,
            y_range=ssn_plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        const x_start = x_range.start;
        const x_end = x_range.end;
        const y_start = y_range.start;
        const y_end = y_range.end;

        // Download data with visible plot names included
        downloadAxes(
          source,
          x_start,
          x_end,
          y_start,
          y_end,
          plots,
          "txt",
          "SSN"
        );
       """,
    )
)

layout = column(
    row(date_range_picker, reset_button),
    ssn_plot.get_plot(),
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)
curdoc().add_root(layout)
