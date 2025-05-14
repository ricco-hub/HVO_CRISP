import math
import numpy as np

from datetime import datetime, timezone, timedelta


def errorbar(
    fig,
    x,
    y,
    yerr=None,
    color="red",
    point_kwargs={},
    error_kwargs={},
    legend_label=None,
):

    points = fig.line(
        x, y, color=color, legend_label=legend_label, line_width=2, **point_kwargs
    )

    error_lines = []

    if yerr is not None:
        y_err_x = []
        y_err_y = []
        for px, py, err in zip(x, y, yerr):
            y_err_x.append((px, px))
            y_err_y.append((py - err, py + err))
        errors = fig.multi_line(y_err_x, y_err_y, color=color, **error_kwargs)
        error_lines.append(errors)

    return points, error_lines


def is_leap_year(year: float) -> bool:
    """
  Determine if year is a leap year
  """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def decimal_year_to_YYYYMMDD(decimal_year: float):
    """
    Convert a year in the form yyyy.xx into YYYY-MM-DD
    Output:
      ymd, a datetime64 object in the form YYYY-MM-DD
  """
    # get integer year
    year = math.floor(decimal_year)

    # get fractional part
    fraction = decimal_year - year

    # determine if it's a leap year
    days_in_year = 366 if is_leap_year(decimal_year) else 365

    # convert the fraction to days
    days = math.floor(fraction * days_in_year)

    # create the date object starting from January 1
    start_of_year = datetime(year, 1, 1, tzinfo=timezone.utc)

    # add the days to get the final date
    final_date = start_of_year + timedelta(days=days)

    ymd = np.datetime64(final_date, "D")

    return ymd


# Create CheckboxGroup with options
# plot_checkbox_group = CheckboxGroup(labels=series_names, active=[])
# error_checkbox_group = CheckboxGroup(
#     labels=[f"{name} (error bars)" for name in series_names], active=[]
# )

# Attach the callback to checkbox group
# plot_checkbox_group.on_change(
#     "active",
#     partial(
#         update_plots, checkbox=plot_checkbox_group, series=series_names, plots=plots
#     ),
# )
# error_checkbox_group.on_change(
#     "active",
#     partial(
#         update_error_bars,
#         checkbox=error_checkbox_group,
#         series=series_names,
#         plots=plots,
#     ),
# )
