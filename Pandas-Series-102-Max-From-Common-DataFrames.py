import pandas as pd
#https://www.codewars.com/kata/5ea2a798f9632c0032659a75/train/python
def max_common(df_a, df_b): 
    new_df = df_a.copy()
    for column in df_a.columns:
        if column in df_b.columns:
            new_df[column] = df_a[column].where(df_a[column] >= df_b[column], df_b[column])
    return new_df