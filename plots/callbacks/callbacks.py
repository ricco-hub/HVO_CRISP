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
    Python callback to update data every time user picks new date range in calendar
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
    source.data = {col: filtered_data[col] for col in filtered_data.columns}


def update_all_sources(
    attr, old, new, date_range, data_dict: dict, sources_dict: dict
) -> None:
    """
    Python callback to update tilt angle datasets every time user picks new date range in calendar
    Inputs:
      date_range, bokeh DateRangePicker object
      data_dict, dictionary containing tilt angle datasets
      sources_dict, dictionary containing tilt angle datasets as bokeh ColumnDataSource objects
    """

    start_date, end_date = date_range.value
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    start_date = datetime.combine(start_date, datetime.min.time())
    end_date = datetime.combine(end_date, datetime.max.time())

    for label, df in data_dict.items():
        filtered = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
        sources_dict[label].data = {col: filtered[col] for col in filtered.columns}


def reset_data(original_data, date_picker) -> None:
    """
    Python callback to reset data in SSN plot after manually manipulating data
    Inputs:
        original_data: pandas DataFrame containing data
        date_picker: bokeh DateRangePicker object
    """

    # convert pd.Timestamp to datetime.date for DateRangePicker
    min_date = original_data["date"].min().date()
    max_date = original_data["date"].max().date()

    date_picker.value = (min_date, max_date)


def reset_all(min_date, max_date, date_picker, data: dict, source_data: dict) -> None:
    """
    Python callback to reset data in tilt angle plots after selecting dates in calendar
    Inputs:
      min_date, datetime.date object representing global minimum date of datasets
      max_date, datetime.date object representing global maximum date of datasets
      date_picker, bokeh DateRangePicker object
      data, dictionary containing tilt angle datasets
      source_data, dictionary containing tilt angle datasets as bokeh ColumnDataSource objects
    """

    date_picker.value = (min_date, max_date)
    for label, df in data.items():
        source_data[label].data = {col: df[col] for col in df.columns}
