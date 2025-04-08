from bokeh.io import curdoc
from bokeh.plotting import figure

p = figure(title="Hello Bokeh", height=300, width=600)
p.line([0, 1, 2], [0, 1, 0])

curdoc().add_root(p)

print("testing testing")
