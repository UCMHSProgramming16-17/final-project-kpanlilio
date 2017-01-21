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
    ('Attack Stat', '@Attack'),
    ('Defense Stat', '@Defense')
]

# create the scatter chart
p = Scatter(df, x='Attack', y='Defense', title="Attack vs. Defense Stats", 
            xlabel="Attack", ylabel="Defense", color='Type 1', tooltips=tooltips)

# create output file
output_file('scatter.html')
# save graph to output file
save(p)