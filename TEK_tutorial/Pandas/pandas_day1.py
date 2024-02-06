# Download libraries
# 1. pandas (pip install pandas)
# 2. Jupyter notebook(pip install notebook)

# We will use the format called "codecell"
# Codecell is inline jupyter converter inside py files.
# %%
1+1
# %%
# how to print your message
print("hello world")

# %%
# Import your libraries
import pandas as pd
# %%
# 1. Creating your dataset in pandas

# 1.1. Creating a single column dataframe
# function: pd.Series()
df1 = pd.Series([1,2,3,4,5,6])
df1
# %%
# 1.2. Creating dataframe with a range value
# function: pd.date_range()
df2 = pd.date_range("20231229","20231231")
df3 = pd.date_range("20231229", periods = 5)
df3
# %%
# 1.3. Creating dataframe with a data dictionary
df4 = pd.DataFrame({"a":[4,5,6],
                    "b":[7,8,9],
                    "c":[10,11,12]})
df4
# %%
df5 = pd.DataFrame([[4,7,10],
                    [5,8,11],
                    [6,9,12]],
                   columns=['a','b','c'])
df5
# %%
# Exercise to create your own dataframe
# first column name = "calories"
# second column name = "duration"
# first column values = 420, 380, 390
# second column values = 50, 40, 45
# %%
calories = [420, 380, 390]
duration = [50, 40, 45]
print(calories, duration)

df6 = pd.DataFrame({"calories": calories,
                    "duration": duration})
df6

# %%
# 2. How to load and import datatables from the other sources
# 2.1. Read csv file
df7 = pd.read_csv("data/data.csv")
df7
# %%
# 2.2. Read json file
df8 = pd.read_json("data/data.json")
df8
# %%

# 2.3. Read excel file(xlsx)
# install library called openpyxl
# pip install openpyxl
import openpyxl
# load your dataset from the xlsx
df9 = openpyxl.load_workbook("data/data.xlsx")
# Chack your sheet name
df9.sheetnames
# Extract sheet into data object
df9_1 = df9['data']
# Extract values inside your data object
df9_1 = df9_1.values
df9_1
# Load your created data object into pandas libary
df9 = pd.DataFrame(df9_1)
df9
# %%
# 3. View your data
df7
# %%
# 3.1. head() and tail()
df7.head(10)
# %%
df7.tail(10)
# %%
# 3.2. print index
df7.index
# %%
# 3.3. print columns
df7.columns
# %%
# 3.4. Summary view of your dataframe
df7.describe()
# %%
# 4. Selecting your data values from the dataframe
# Create df10 data object with the imported EAI.csv file.

# %%
# TASK1. READ THE EAI.CSV FILE
df10 = pd.read_csv("data/EAI.csv")

# %%
# TASK2. PRINT OUT COLUMN NAMES
df10.columns
# %%
# TASK3. PROVIDE SUMMARY VIEW OF YOUR DF10
df10.describe()
# %%
# TASK4. Do random sampling of your DF10
df10.sample(frac=0.1)
# %%
# 4.1. Select your columns
df10["Annual Salary"]
# %%
# 4.2. Select your rows
df10[10:20]
# %%
# 4.3. Select your rows with columns
df10.loc[10:15, ["Annual Salary", "Training Program"]]
# %%
# 5. Filtering selection of your dataframe
# 5.1. Filter based on numeric condition
# = you will filter your dataframe by condition.
df10[df10["Annual Salary"] > 54577]
# %%
# 5.2. Filter based on string condition
df10["Training Program"].isin(["Yes"])
# %%
df10[df10["Training Program"].isin(["Yes"])]
# %%
# Exercise
# Please filter out your EAI.csv file with the following conditions.
# Condition1: managers having annual salary less than 45,000 USD.
# Condition2: managers who said they didn't take training program.
df10.describe()
# %%
# Second best solution
df10_1 = df10[df10["Annual Salary"] < 45000]
df10_1[df10_1["Training Program"].isin(["No"])]
# %%
# Best solution
df10[(df10["Annual Salary"] < 45000) & (df10_1["Training Program"].isin(["No"]))]
# %%
