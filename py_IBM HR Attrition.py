# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================
# 2. Load Dataset
# ==============================
# Download CSV from Kaggle and update path
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Preview data
print(df.head())
