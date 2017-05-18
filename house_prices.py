import pandas as pd
from pandas import DataFrame
import datetime

data_boroughs = pd.read_csv("london_boroughs.csv")
boroughs = DataFrame(data_boroughs, columns =["name"])

data = pd.read_csv("Average-prices-2017-02.csv")
df = DataFrame(data, columns =["Date", "Region_Name", "Average_Price"])

df.Region_Name = df.Region_Name.replace("City of Westminster", "Westminster")
df.Region_Name = df.Region_Name.replace("Kensington And Chelsea", "Kensington and Chelsea")
df.Average_Price = df.Average_Price.astype(int)
df.rename(columns={"Region_Name": "name"}, inplace=True)

df = pd.merge(boroughs,df)

df.Date = pd.to_datetime(df.Date)
df.index = df.Date
grouped=df.groupby([(df.index.year), (df.name)]).mean().astype(int)
grouped = grouped.reset_index()
grouped.rename(columns={"level_0": "date"}, inplace=True)
grouped.to_csv("house_prices.csv", index = False)
