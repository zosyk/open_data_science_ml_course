import pandas as pd

data = pd.read_csv('data/beauty.csv', sep=';')

print(type(data))

print(data.head())