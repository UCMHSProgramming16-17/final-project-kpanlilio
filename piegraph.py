# import modules
import csv
import pandas as pd
import bokeh

# read csv dataframe
df = pd.read_csv('Pokemon.csv')

# import necessary plotting imports
from bokeh.charts import Donut, output_file, save
# import color palette 
from bokeh.palettes import plasma

# set up the bar graph components
sab = Donut(df, label='Type 1', values='#', title='Frequency of Pokemon Types', text_font_size='7pt', hover_text='#', palette=plasma(18))

# create output file
output_file('piegraph.html')
# save the pie graph to file
save(sab)

