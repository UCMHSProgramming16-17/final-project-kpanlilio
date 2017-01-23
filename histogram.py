# import needed modules
import csv
import pandas as pd
import bokeh

# read csv data
df = pd.read_csv('Pokemon.csv')

# import necessary visual imports
from bokeh.charts import Histogram, output_file, save

# set up the histogram
p = Histogram(df, values='HP', bins=25, title="HP Distribution in Pokemon (25 bins)", color='teal')

# create the output file
output_file("histogram.html")

# save the histogram to the output file to create it
save(p)