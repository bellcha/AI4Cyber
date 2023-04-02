import pandas as pd

df = pd.read_json('response.json')

df.to_csv('alienvault.csv')