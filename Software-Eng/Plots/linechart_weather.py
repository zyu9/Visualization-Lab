import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data = [go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='actual max temp')]

# Preparing layout
layout = go.Layout(title= 'Actual Maximum Temperature ',
                   xaxis_title= "Month", yaxis_title= "Actual Max Temp")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechartWeather.html')