import ipywidgets as widgets
from IPython.display import display

a = widgets.IntText(value=0, description='A:')
b = widgets.IntText(value=0, description='B:')
out = widgets.Output()

def compute(change):
    with out:
        out.clear_output()
        print(f"Sum: {a.value + b.value}")

a.observe(compute, names='value')
b.observe(compute, names='value')

display(a, b, out)
