import pandas as pd
import plotly.express as px

df = pd.read_csv("E:/WHITEHAT JR/python/P-103/Data.csv")
fig = px.line(df,y = "cases", x = "date",color = "country", title = "Covid")
fig.show()