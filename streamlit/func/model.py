from func.data import load_data, mod_colnames

# customized functions
def sample_dist_cal(n,num,data,colname):
    df=load_data(data)
    df=mod_colnames(df)
    lst1=[]
    lst2=[]
    # Sampling
    for i in range(num):
        df_sampl=df.sample(n=n)
        sample=list(df_sampl[colname])
    # lst1=sample
        lst1.append(sample)
    # Calculating sampling mean
        sample_m=df_sampl[colname].mean()
        lst2.append(sample_m)
    #lst2=sample_m
    return lst1, lst2

# %%
