import pandas as pd
#https://www.codewars.com/kata/5e60cdcd01712200335bd676/train/python
def rename_columns(df, names):  
    new_df = df.copy()
    new_df.columns = names
    return new_df