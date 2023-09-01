# %%
# pip install openpyxl
import pandas as pd
eai_excel=pd.read_excel('EAI.xlsx')
eai_csv=pd.read_csv('EAI.csv')
eai_excel.head()

# %%
eai_csv.head()
# %%
import pydataset
# Look up the pydataset library and find a list of available datasets
pydataset.data()

df=pydataset.data('titanic')
df.head()
# %%
eai_csv.describe()
# %%
eai_csv.head()
# %%
