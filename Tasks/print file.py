# %%


# %% [markdown]
# # Participants
# 
# Title = "Scholar"
# 
# Name = "Muhammad Faizan Arshad"
# 
# Email = "faizanarshad124@gmail.com"
# 
# Whatsapp = "+923205501341"
# 
# 

# %%

import pandas as pd
import numpy as np
dates = pd.date_range("20211010", periods=6)
dates
df = pd.DataFrame(np.random.rand(6,4),index= dates,columns = list("ABCD"))
df

# %%
df2 = pd.DataFrame(
    {
        "A":  1.0,
        "B":  pd.Timestamp("20210605"),
        "C" : pd.Series(1,index=list(range(4)),dtype="float32"),
        "D" : np.array([3]*4, dtype="int32"),
        "E" : pd.Categorical(["girl","women","girl","women"]),
        "F": "female"
    }
)
df2

# %% [markdown]
# > Dtype is the code use to know the type of the veriable

# %%
df2.dtypes

# %% [markdown]
# To know the data set aur preview it we use the two commands

# %%
df2.head()

# %% [markdown]
# 

# %%
df.head(1)

# %%
df2.index

# %%
df.to_numpy()

# %%
df2.to_numpy()

# %%
df2.sort_values(by="C",ascending=True)

# %%
df[0:2]

# %%
df.loc[dates[0]]

# %%
df2.loc[:,["A","B"]]

# %%
df.head

# %%
df.loc["20211010":"20211015",["A","B"]]

# %%
df.loc["20211010",["A","B","C","D"]]

# %%
df.iloc[3]

# %%
df.iloc[: ,0:3]

# %%
df.iloc[0:3 ,:]

# %%
df[df["A"]>0.1]

# %%
df2["new"]=[1,2,1,2]


