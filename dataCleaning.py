import pandas as pd
# import numpy as np

def run():
    df = pd.read_csv('https://raw.githubusercontent.com/DependerKumarSoni/Naive-Bayes/main/adult.csv',header=None)
    return df

df = run()
print(df.head())