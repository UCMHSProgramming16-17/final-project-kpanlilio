# module
import csv
import pandas as pd
import numpy as np
import bokeh

# read and get data
df = pd.read_csv('Pokemon.csv')

# import necessary common inputs for visual
from bokeh.charts import Scatter, output_file, save

# create the scatter chart
p = Scatter(df, x='Attack', y='Defense', title="Attack vs. Defense Stats", 
            xlabel="Attack", ylabel="Defense", color='Type 1', marker='Type 1')

# create output file
output_file('scatter.html')
# save graph to output file
save(p)


# #import module
# import csv
# import pandas as pd
# import numpy as np
# import bokeh

# # read data
# df = pd.read_csv('Pokemon.csv')

# from bokeh.charts import Bar, output_file, save

# graph = Bar(df, 'Type 1', values='#', title='Frequency of Pokemon Types', color='pink')

# output_file('scatterplot.html')
# save(graph)