from bokeh.embed import components
from bokeh.plotting import figure


# Create a basic scatter plot
plot = figure(title="Example Bokeh Plot", x_axis_label='X', y_axis_label='Y')
plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=10, color="navy", alpha=0.5)

script, div = components(plot)