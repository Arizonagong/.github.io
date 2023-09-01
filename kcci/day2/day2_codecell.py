print("hello world")

# %%
2**2
# %%
15 % 2
# %%
'fall'
# %%
fall
# %%
print('fall')
# %%
'K'+2*'c'+'i'
# %%
print('K'+2*'c'+'i')
# %%
print('py''thon')
# %%
a=1
b=2
a,b
# %%
a+b
# %%
c="John"
b="10 years old"
print(c,":",b)
# %%
b.replace('10','12')
# %%
b.split(' ')

# %%
txt = "     banana     "
txt.strip()

# %%
txt = ' John '
print('[' + txt.rstrip() + ']')
print('[' + txt.lstrip() + ']')
print('[' + txt.strip() + ']')
# %%
phone1='800-294-2934'
phone2='800-293-4920'
phone3='602-493-2999'
a=phone1.replace('-','')
b=phone2.replace('-','')
c=phone3.replace('-','')
a,b,c

# %%
a=[1,2]
a.sum()
# %%
a='1'
b='2'
'_'.join([a,b])
# %%
c="John"
b="10 years old"
print(c,":",b)
c=b.split(' ')
d=' '.join(c)
d

# %%
word='Python'
word[0]

# %%
word[:2]
word[:6]
# %%
d = '8002942934'
'-'.join([d[:3], d[3:6], d[6:]])

# %%
x='selflearning'
'-'.join([x[:4], x[4:12]])

# %%
name=['John','Jane','Jason']
age=[13,14,15]
gender=['male','female','male']
print(name, age, gender)

# %%
import pandas as pd
data={'name':name,
'age':age,
'gender':gender}

df=pd.DataFrame.from_dict(data)
print(df)

# %%
data={'name':name,
'age':age,
'gender':gender}
data
# %%
list = ['physics', 'chemistry', 1997, 2000];

# %%
list

# %%
list[0]
# %%
list[:3]
# %%
import pandas as pd
patient_name=['Pollck', 'James', 'Sophia', 'John', 'Duke']
contact=['602-420-4928', '666-423-4938', '555-242-4582', '222-444-5824', '492-222-5827']
age=[45,22,44,32,42]
#Create dictionary
data={'patient_name':patient_name,'contact':contact,'age':age}
#Create dataframe
df_hosp=pd.DataFrame.from_dict(data)
print(df_hosp)
# %%
import pydataset
# Look up the pydataset library and find a list of available datasets
pydataset.data()

df=pydataset.data('titanic')
print(df)
df.describe()
df.info()
# %%
eai_excel=pd.read_excel('EAI.xlsx')
# %%
