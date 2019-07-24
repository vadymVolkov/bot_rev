import pandas as pd

df = pd.read_csv('db.csv', sep=',')
dicts = df.to_dict().values()
print(dicts)