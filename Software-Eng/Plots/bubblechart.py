import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronavirusTotal.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating unrecovered column
df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Removing China and Others from data frame
df = df[(df['Country'] != 'China') & (df['Country'] != 'Others')]

# Creating sum of number of cases group by Country Column
new_df = df.groupby(['Country']).agg(
    {'Confirmed': 'sum', 'Recovered': 'sum', 'Unrecovered':'sum'}).reset_index()

# Preparing data
data = [
    go.Scatter(x=new_df['Recovered'],
               y=new_df['Unrecovered'],
               text=new_df['Country'],
               mode='markers',
               marker=dict(size=new_df['Confirmed']/100,
                color=new_df['Confirmed']/100, showscale=True))
]

# Preparing layout
layout = go.Layout(title= 'Corona Virus Confirmed Cases',
                   xaxis_title="Recovered Cases", yaxis_title="Unrecovered Cases",
                   hovermode='closet')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')