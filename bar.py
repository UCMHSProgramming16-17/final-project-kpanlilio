# import necessary modules
import csv
import pandas as pd
import bokeh

# import/ read the csv file
df = pd.read_csv('Pokemon.csv')

# import the necessary visual imports
from bokeh.charts import Bar, output_file, save

# set up the bar graph visuals
p = Bar(df, 'Generation', color='Generation', legend='top_right', title="Number of Pokemon per Generation")

# create the output file
output_file("bar.html")

# save bar graph to output file
save(p)

