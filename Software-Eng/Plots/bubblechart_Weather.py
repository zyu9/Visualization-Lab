import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'sum', 'average_max_temp': 'sum'}).reset_index()

# Preparing data
data = [
    go.Scatter(x=new_df['month'],
               y=new_df['average_min_temp'],
               text=new_df['average_max_temp'],
               mode='markers',
               marker=dict(size=new_df['average_min_temp']/100,
               color=new_df['average_min_temp']/100,
               showscale=True))
]

# Preparing layout
layout = go.Layout(title= 'Average min and max temperature of each month',
                   xaxis_title="Month", yaxis_title="Average temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechartWeather.html')