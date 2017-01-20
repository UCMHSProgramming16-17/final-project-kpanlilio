#import module
import csv
import pandas as pd
import bokeh

# read data
df = pd.read_csv('Pokemon.csv')

from bokeh.charts import Donut, output_file, save

from bokeh.palettes import plasma

sab = Donut(df, label='Type 1', values='#', title='Frequency of Pokemon Types', text_font_size='7pt', hover_text='#', palette=plasma(18))

output_file('piegraph.html')
save(sab)

# #import module
# import csv
# import pandas as pd
# import numpy as np
# import bokeh

# # read data
# df = pd.read_csv('Pokemon.csv')

# from bokeh.charts import Donut, output_file, save
# sab = Bar(df, 'Type 1', values='#', title='Frequency of Pokemon Types', color='pink')

# output_file('sab.html')
# save(sab)