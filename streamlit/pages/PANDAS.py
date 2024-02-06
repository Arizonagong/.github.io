import pandas as pd
import streamlit as st
from func.data import load_data

df=load_data("EAI")
st.dataframe(df)
st.table(df)
#%%
import pandas as pd
data_df = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    }
)
data_df
# %%
