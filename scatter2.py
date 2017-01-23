# module
import csv
import pandas as pd
import numpy as np
import bokeh

# read and get data
df = pd.read_csv('Pokemon.csv')

# import necessary common inputs for visual
from bokeh.charts import Scatter, output_file, save

# add information to the hover tool
tooltips=[
    ('Name', '@Name'),
    ('Generation', '@Generation'),
]

# create the scatter chart
p = Scatter(df, x='Sp. Atk', y='Sp. Def', title="Attack vs. Defense Stats (Color-coded by Generation)", 
            xlabel="Special Attack", ylabel="Special Defense", color='Generation', tooltips=tooltips)

# create output file
output_file('scatter2.html')
# save graph to output file
save(p)