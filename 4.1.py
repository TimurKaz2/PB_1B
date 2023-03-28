import pandas as pd 
df = pd.read_csv('precious_metal.csv', sep=';') 
print(df)

print(df.info())
