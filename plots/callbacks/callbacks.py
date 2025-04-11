import pickle
import pandas as pd
import json

from datetime import datetime
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Button
from bokeh.layouts import column


def update_plots(attr, old, new, checkbox, series: list, plots: dict) -> None:
    """
    Callback function to update the visibility of scatter plots for SSN
    Inputs:
        checkbox: bokeh CheckboxGroup object
        series: column data names
        plots: dictionary of pre-made scatter plot data
    """

    # Get the selected indices from checkbox group
    active_indices = checkbox.active

    # Update visibility for each plot and error bars
    for i, name in enumerate(series):
        is_active = i in active_indices
        plots[name]["scatter"].visible = is_active


def update_error_bars(attr, old, new, checkbox, series: list, plots: dict) -> None:
    """
    Callback function to update visibility of error bars for SSN
    Inputs:
        checkbox: bokeh CheckboxGroup object
        series: column data names
        plots: dictionary of pre-made scatter plot data
    """

    # Get selected indices from checkbox group for error bars
    active_indices = checkbox.active

    # Update visibility for each error bar set
    for i, name in enumerate(series):
        is_active = i in active_indices
        for line in plots[name]["error_bars"]:
            line.visible = is_active


def update_hover_data(attr, old, new, date_range, data, source) -> None:
    """
    Python callback to update SSN data every time user picks new date range in calendar
    Inputs:
        date_range: bokeh DateRangePicker object
        data: pandas DataFrame containing data
        source: bokeh ColumnDataSource
    """

    # Get the date range selected in the DateRangeSlider
    start_date, end_date = date_range.value

    # convert to datetime.date
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    # convert to datetime.datetime
    start_date = datetime.combine(start_date, datetime.min.time())
    end_date = datetime.combine(end_date, datetime.max.time())

    # Filter the data based on the selected date range
    filtered_data = data[(data["date"] >= start_date) & (data["date"] <= end_date)]
    # Update the data source with filtered data
    source.data = {
        "year": filtered_data["year"],
        "month": filtered_data["month"],
        "day": filtered_data["day"],
        "dec_year": filtered_data["decimal year"],
        "ssn_value": filtered_data["SNvalue"],
        "ssn_err": filtered_data["SNerror"],
        "num_obs": filtered_data["Nb observations"],
        "status": filtered_data["Status"],
    }


def reset_data(original_data, date_picker) -> None:
    """
    Python callback to reset data in SSN plot after manually manipulating data
    Inputs:
        original_data: pandas DataFrame containing data
        date_picker: bokeh DateRangerPicker object
    """

    # convert pd.Timestamp to datetime.date for DateRangePicker
    min_date = original_data["date"].min().date()
    max_date = original_data["date"].max().date()

    date_picker.value = (min_date, max_date)
