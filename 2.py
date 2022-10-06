import pandas as pd
df = pd.read_csv('chicago.csv')
print((df.count()[0]) - 50)
