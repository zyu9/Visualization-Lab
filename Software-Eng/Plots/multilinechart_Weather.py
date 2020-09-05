import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
trace1 = go.Scatter(x=df['month'], y=df['actual_max_temp'], mode='lines', name='actual max temp')
trace2 = go.Scatter(x=df['month'], y=df['actual_mean_temp'], mode='lines', name='actual mean temp')
trace3 = go.Scatter(x=df['month'], y=df['actual_min_temp'], mode='lines', name='actual min temp')
data = [trace1,trace2,trace3]

# Preparing layout
layout = go.Layout(title= 'Actual Temperature',
                   xaxis_title= "Month", yaxis_title= "Actual Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechartWeather.html')