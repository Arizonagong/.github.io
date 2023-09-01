---
marp: true
paginate: true
class:
  - invert
---
# **VScode and Python**
## Day4: Data Manipulation in Pandas

Dr. Byoung-gyu Gong
Assistant professor 
Information System
Davide Eccles School of Business
University of Utah Asia Campus

---

# Contents
- Changing Values in the Dataframe
  - Changing column names
  - Changing values 
  - Changing values by condition
- Subseting and Merging Dataframes
  - Subsetting and Spliting
  - Merging with Keys

---

 # Changing Values in the Dataframe
  - Changing column names
  - Changing values 
  - Changing values by condition

---

## Changing Column Names

### Loading CSV file
```python
# Load pandas library
import pandas as pd

# Import csv dataset
df=pd.read_csv('EAI.csv')
df.head()
```

---
### Checking Column Names

- Conventionally, white space, other symbols, and capital letters in the column names are not appropriate as some functions may not recognize such a format as an input.

```python
# Print column names
list(df.columns)
```
- In the example, you may find column names inlcude white space.
- Usually, it is recommended to replace the white space with '_'.

---
## dataframe.rename(columns={'old name':'new name'})
```python
df.rename(columns={'Manager':'manager',
                   'Annual Salary': 'annual_salary',
                   'Training Program': 'training_program'},
                   inplace=True)

list(df.columns)
```
- 'inplace=True' means you are replace old dataframe with your modified version. If you don't set it as true, then your existing dataframe is not changed, and python only present copy of the original version.
---

## Changing values 
- Now, we found that there is end-of-the-year bonus was given to the entire managers. That amount is 5000. That should be added to the annual salary.
- Then, how can we make such a change?
```python
# Let's check up our dataframe again.
df.head()
```
---

## Changing Numeric Values
### apply(lambda x: formula)
- lambda declares that all column values will be considered x in the formula.
```python
df['annual_salary'] = df['annual_salary'].apply(lambda x: x+5000)
```
---
## Changing String Values
- Now, we'd like to change string values. We want 'training" column to include lower case strings.
### apply(lambda x: formula including x)
- lambda declares that all column values will be considered x in the formula.
```python
df['training_program'] = df['training_program'].apply(lambda x: x.lower())
```

---
## Changing values by condition
- Let's assume that the company decided to give 10,000 USD bonus based on their participation in the training program.
- It may require us to add 10,000 in the annual salary only of the managers who participated in the training program.

---
- apply(lambda x) function can include if-else conditional state.
- Adding 'axis' arguement at the end is very critical. 'axis=1' means applying the function to each columns, while 'axis=0' means applying the function to each rows.
```python
df['new_annual_salary'] = df[['annual_salary','training_program']].
                            apply(lambda x: 
                              x['annual_salary']+10000 
                              if x['training_program']=="yes" 
                              else x['annual_salary'], 
                            axis=1)
df.head()

```

---
# Subseting and Merging Dataframes
  - Subsetting and Spliting
  - Merging with Keys

---

## Subsetting and Spliting
1. Deleting column: df.drop()
```python
df.head()
```
```python
df.drop(['annual_salary'], axis=1, inplace=True)
```
2. Selecting columns
```python
df[['new_annual_salary']]
```

---

3. Splitting and joining columns
- Let's think of a request to split string values in specific column.
- We can use str[]function with indexing skill we learned before.
```python
df['training_program_1']=df['training_program'].str[:1]
df['training_program_2']=df['training_program'].str[1:2]
df['training_program_3']=df['training_program'].str[2:]

```
- Then we can join each column strings with simple arithmatic combination.
```python
df['number']=df['number1'] + '-' + df_phone['number2'] + '-' + df_phone['number3']
```

---
4. Subsetting rows
```python
# filtering by condition: apply(lambda)
df.apply(lambda x: x[df['training_program']=='yes'])

# Subsetting by index
df[:3]
```

---
## Merging with keys

```python
# Let's assume that we have two different data set stored separately
df_tp=df[['manager','training_program']]
df_as=df[['manager','new_annual_salary']]
```
```python
# Now we want to merge them based on the same ID of managers
df_tp.merge(df_as, how='inner', on='manager')
```

---
# Excercise -Question
Let's go back to our phone number example.
```python
phone=['phone1','phone2','phone3']
number=['800-294-2934','800-293-4920','602-493-2999']
data={'phone':phone,
      'number':number}
df_phone=pd.DataFrame.from_dict(data)
df_phone
```
- How can you delete '-'(hyphen) in the middle of the column 'number'?