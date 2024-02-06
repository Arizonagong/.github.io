# --- CAUTION --- # 
# YOU NEVER EXECUTE THE CODE IN THIS FILE.
# YOU JUST SAVE THIS FILE AND REFRESH YOUR WEBPAGE IN YOUR WEB BROSER.
# TERMINATE YOUR WEBSITE: CTRL + C

# install the libraries
# pip install streamlit
# pip install pandas
import streamlit as st 
import pandas as pd

# 1. Let's create our first app
st.title('Manager Salaries')
# Run your first app. 
# EXECUTE THE CODE IN YOUR TERMINAL: "streamlit run table.py"

# 2. Write down some description of this app.
st.text("This is a toy example webpage for the TEK club tutorial session.")
st.text("The table here is about the manager's salaries of a certain company and their training program participation.")

# ----. import datafile

# 3.1. Read your data file
df = pd.read_csv("EAI.csv")
max_val=df["Annual Salary"].max()
min_val=df["Annual Salary"].min()

# 3.2. Create summary table and load it.
df_sum = df.describe()


# ----. Apply input widgets
# Column Filter

options = st.multiselect('Select Columns',df.columns)
st.write('You selected:', options)

# Row filter1: By index number
#rows = st.slider('How Many First Rows Do you Want to Read', 0, 10, 10)
#st.write("I'd like to print upto ", rows, 'rows')

#if rows > 0:
#    df=df.head(n=rows)

# Row filter2: By value for each column

maxval = st.slider('How Many First Rows Do you Want to Read', float(min_val), float(max_val), float(min_val))
st.write("I'd like to print upto ", maxval, 'rows')

if maxval > min_val:
    df=df[df["Annual Salary"] < maxval]

# 3. Wrtie down your data table.



# 4. Change the layout of your webpage: Add columns
    
# 5. Change the layout of your webpage: Add tabs
tab1, tab2 = st.tabs(["raw data", "summary data"])
with tab1:
    st.write("Length of your data frame: ",len(df))
    st.dataframe(df)
with tab2: 
    st.dataframe(df_sum)