# %%
import pandas as pd
import seaborn as sns
# %%
titanic=sns.load_dataset('titanic')
titanic.head()
# %%
# Countplot
sns.catplot(x ="sex", hue ="survived",
kind ="count", data = titanic)
# %%
# Violinplot Displays distribution of data
# across all levels of a category.
sns.violinplot(x ="sex", y ="age", hue ="survived",
data = titanic, split = True)
# %%
sns.catplot(x ="pclass", y ="fare", hue ="survived",
data = titanic, kind='box')
# %%
sns.catplot(x ="survived", y ="pclass", hue ="survived",
data = titanic)
# %%
sns.catplot(data=titanic, x="sex", y="survived", hue="pclass")
# %%
