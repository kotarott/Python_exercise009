import pandas as pd

df = pd.DataFrame(columns=["A", "B"])
df = df.append({"A":"a", "B":"b"}, ignore_index=True)
print(df)