import pandas as pd

df = pd.read_csv('final.csv')
df = df.drop(['name'], axis=1)

df.to_csv('final2.csv', index=False)
