import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df['Date'] = pd.to_datatime(df['Date'])

# Preparing data
data = [go.Scatter(x=df['Date'], y=df['Confirmed'], mode= 'lines', name= 'Death')]

# Preparing layout
layout = go.Layout(title= 'Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17',
                   xaxis_title= "Date", yaxis_title= "Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')