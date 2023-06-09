import pandas as pd
import pyodide

raw_path='https://raw.githubusercontent.com/adammielniczuk/dash/main/dashboard/data'

df=pd.read_csv(pyodide.htpp.open_url(raw_path+"/city_late.csv"), sep=';')

df['average % of trains on time'] = df.iloc[:, 1:].mean(axis=1)*100
df = df[['station', 'average % of trains on time']]
df['average % of trains on time'] = df['average % of trains on time'].round(2).astype(str) + '%'
print(df)