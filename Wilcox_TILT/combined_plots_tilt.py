import pandas as pd
import sys
import os

from datetime import datetime
from pathlib import Path
from functools import partial
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, DateRangePicker, Button, CustomJS
from bokeh.plotting import curdoc
from bokeh.palettes import Category10

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from plots.hvo_plots import HVOPlot
from plots.callbacks.callbacks import (
    update_hover_data,
    reset_data_combined,
    sync_hover_tool_icon,
)
from utils.utils import decimal_year_to_YYYYMMDD


# --- Load data ---
northern_l = pd.read_pickle("data/Tilt_L_n.pkl")
northern_r = pd.read_pickle("data/Tilt_R_n.pkl")
southern_l = pd.read_pickle("data/Tilt_L_s.pkl")
southern_r = pd.read_pickle("data/Tilt_R_s.pkl")
average_l = pd.read_pickle("data/Tilt_L_av.pkl")
average_r = pd.read_pickle("data/Tilt_R_av.pkl")

# Create datetime columns
northern_l["date"] = northern_l["decimal_year"].apply(decimal_year_to_YYYYMMDD)
northern_r["date"] = northern_r["decimal_year"].apply(decimal_year_to_YYYYMMDD)
southern_l["date"] = southern_l["decimal_year"].apply(decimal_year_to_YYYYMMDD)
southern_r["date"] = southern_r["decimal_year"].apply(decimal_year_to_YYYYMMDD)
average_l["date"] = average_l["decimal_year"].apply(decimal_year_to_YYYYMMDD)
average_r["date"] = average_r["decimal_year"].apply(decimal_year_to_YYYYMMDD)

# Bundle all data
data_dict = {
    "Northern (L)": northern_l,
    "Northern (R)": northern_r,
    "Southern (L)": southern_l,
    "Southern (R)": southern_r,
    "Average (L)": average_l,
    "Average (R)": average_r,
}
y_keys = ["L_n", "R_n", "L_s", "R_s", "L_av", "R_av"]

# --- Plot setup ---
plot = HVOPlot(
    "Tilt Angle of Heliospheric Current Sheet", "Time (years)", "Angle (degrees)"
)
sources = {}
source_data = {}
plots = {}
colors = Category10[10]

# Create all line plots
for i, (label, df) in enumerate(data_dict.items()):
    sources[label] = ColumnDataSource(data=df)
    source_data[label] = ColumnDataSource(data=df.drop(columns=["date"]))

    scatter = plot.line_plot(
        sources[label],
        legend_label=label,
        x="decimal_year",
        y=y_keys[i],
        color=colors[i],
    )
    hover = plot.add_hover_tool(
        sources[label], "decimal_year", y_keys[i], "Year", "Angle", colors[i],
    )
    plots[label] = {"scatter": scatter, "hover": hover}

plot.set_click_policy()

# Toggle visibility of HoverTool based on visibility of plots
for label, obj in plots.items():
    obj["scatter"].on_change(
        "visible", partial(sync_hover_tool_icon, plots=plots, plot=plot)
    )

# --- DateRangePicker ---
# Convert to native datetime.date objects
min_date = min(df["date"].min() for df in data_dict.values()).date()
max_date = max(df["date"].max() for df in data_dict.values()).date()

date_range_picker = DateRangePicker(
    title="Select date range manually. Double click to select a date.",
    value=(min_date, max_date),
    min_date=min_date,
    max_date=max_date,
)


# Attach callback to filter all sources
for label, df in data_dict.items():
    date_range_picker.on_change(
        "value",
        partial(
            update_hover_data,
            date_range=date_range_picker,
            data=df,
            source=sources[label],
        ),
    )

# --- Reset button ---
reset_button = Button(label="Reset Plot", button_type="primary")
reset_button.on_click(
    partial(
        reset_data_combined,
        data_dict=data_dict,
        sources=sources,
        date_picker=date_range_picker,
    )
)


# --- Download buttons ---
download_csv_button = Button(label="Download CSV Data", button_type="success")
download_txt_button = Button(label="Download TXT Data", button_type="success")

js_callbacks = (
    Path(__file__).parent.parent / "plots" / "callbacks" / "callbacks.js"
).read_text("utf8")

download_csv_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.get_plot().x_range,
            y_range=plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        downloadAxes(source, x_range.start, x_range.end, y_range.start, y_range.end, plots, "csv", "Tilt");
        """,
    )
)

download_txt_button.js_on_click(
    CustomJS(
        args=dict(
            source=sources,
            plots=plots,
            x_range=plot.get_plot().x_range,
            y_range=plot.get_plot().y_range,
        ),
        code=js_callbacks
        + """
        downloadAxes(source, x_range.start, x_range.end, y_range.start, y_range.end, plots, "txt", "Tilt");
        """,
    )
)

# --- Layout ---
layout = column(
    row(date_range_picker, reset_button),
    plot.get_plot(),
    row(download_csv_button, download_txt_button),
    sizing_mode="stretch_both",
)

curdoc().add_root(layout)
