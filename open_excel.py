import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")  # or your dataset name
df.head()
df.to_excel("output.xlsx", index=False)