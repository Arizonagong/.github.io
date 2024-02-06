import pandas as pd
import numpy as np

# Load your data set
def load_data(data):
    #data_name="data/"+data+".csv"
    df = pd.read_csv("data/"+data+".csv")
    df = df.reset_index(drop=True)
    return df

# Modify your column names
def mod_colnames(data):
    data.columns = data.columns.str.replace(" ", "_", regex=True)
    return data
