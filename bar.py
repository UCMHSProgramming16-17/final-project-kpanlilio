import csv
import pandas as pd
import bokeh

df = pd.read_csv('Pokemon.csv')

from bokeh.charts import Histogram, output_file, save