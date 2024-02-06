# %%
import pandas as pd
phone=['phone1','phone2','phone3']
number=['800-294-2934','800-293-4920','602-493-2999']
data={'phone':phone,
      'number':number}
df_phone=pd.DataFrame.from_dict(data)
df_phone
# %%
df_phone['number']=df_phone['number'].str.replace('-','')
df_phone
# %%
df_phone['number1'],df_phone['number2'],df_phone['number3']=df_phone['number'].str[:3],df_phone['number'].str[3:6],df_phone['number'].str[6:]
df_phone['number']=df_phone['number1'] + '-' + df_phone['number2'] + '-' + df_phone['number3']
df_phone
# %%
# Load pandas library
import pandas as pd

# Import csv dataset
df=pd.read_csv('EAI.csv')
df
list(df.columns)
# %%
df.rename(columns={'Manager':'manager','Annual Salary': 'annual_salary','Training Program': 'training_program'}, inplace=True)
# %%
df.head()
# %%
a=239882.1232
"{:,.0f}".format(239882.1232)
# %%
df['annual_salary'] = df['annual_salary'].apply(lambda x: x+2)
# %%
df['annual_salary']
# %%
describe(df)
# %%
df.describe()
# %%
df['annual_salary'].describe()
# %%
df['annual_salary'] = df['annual_salary'].apply(lambda x: x+5000)
df.head()
# %%
df['training_program'] = df['training_program'].apply(lambda x: x.lower())
df.head()
# %%
df['new_annual_salary'] = df[['annual_salary','training_program']].apply(lambda x: x['annual_salary']+10000 if x['training_program']=="yes" else x['annual_salary'], axis=1)
df.head()
# %%
df.drop(['annual_salary'], axis=1, inplace=True)
df.head()
# %%
df[['new_annual_salary']]
# %%
df.filter(training_program='yes', axis=0)
# %%
df.apply(lambda x: x[df['training_program']=='yes'])
# %%
df[:3]

# %%
df.head()
# %%
df_tp=df[['manager','training_program']]
df_as=df[['manager','new_annual_salary']]
# %%
df_tp.merge(df_as, how='inner', on='manager')
# %%
df['training_program_1']=df['training_program'].str[:1]
df.head()
# %%
df['training_program_1']=df['training_program'].str[:1]
df['training_program_2']=df['training_program'].str[1:2]
df['training_program_3']=df['training_program'].str[2:]
df.head()
# %%
df['training_program_new']=df['training_program_1'] + '-' + df['training_program_2'] + '-' + df['training_program_3']
df.head()
# %%
import pandas as pd
eai = pd.read_csv("EAI.csv")
eai
# %%
eai[(eai["Annual Salary"] > 40000) & (eai["Training Program"].isin(["No"]))]
# %%
