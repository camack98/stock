import pandas as pd

def calculate(df):
    df = df.tail(30)
    return df.close.mean()
