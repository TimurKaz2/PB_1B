import pandas as pd 
df = pd.read_csv('precious_metal.csv', sep=';') 
print(df)

print(df.info())

df.set_axis(['gold', 'silver', 'platinum', 'palladium', 'date'], axis='columns', inplace = True)

print(df.info())

df.isnull().sum()
print(df)

df.fillna(0)
print(df)