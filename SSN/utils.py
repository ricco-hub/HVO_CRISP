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
