import pandas as pd
df = pd.read_csv('./cycle_3/iris.csv')
print(f"shape of dataset: {df.shape}")
print("first 5 and last 5 data setlist \n ",df)
print(f"dataset size {df.size}")
print(f"no of samples {df.count()}")
print(f"Description of dataset {df.describe()}")