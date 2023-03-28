import pandas as pd 
df = pd.read_csv('precious_metal.csv', sep=';') 
df.set_axis(['gold', 'silver', 'platinum', 'palladium', 'date'], axis='columns', inplace = True)
df.isnull().sum()

df.fillna(0)
print(df)

df['gold'] = df['gold'].apply(lambda x: float(str(x).replace(',','.'))) 
df['silver'] = df['silver'].apply(lambda x: float(str(x).replace(',','.'))) 
df['platinum'] = df['platinum'].apply(lambda x: float(str(x).replace(',','.'))) 
df['palladium'] = df['palladium'].apply(lambda x: float(str(x).replace(',','.'))) 
 
print(df)
