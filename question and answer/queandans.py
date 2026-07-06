import pandas as pd
import numpy as np

pf = pd.read_csv(r"D:\pythonfiles\__pycache__\question and answer\ipseity-daily-responses.csv",index_col=0)
pf.head()


pf.describe()