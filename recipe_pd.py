import numpy as np
import pandas as pd
titanic = pd.read_csv("./data/titanic.csv", index_col="PassengerId")
census = pd.read_csv("./data/census2015.csv", names=["cat01_code", "type", "cat02_code", "hidden_flg", "area_code", "area_name", "unit", "value"], skiprows=1, dtype={"area_code": object})

#===================
# Series
#===================

#===== prepare =====
x = pd.Series([1, 2, 3, 4, 5])
y = titanic["Name"][:10]

#===== attributes =====
x.values # np.ndarray
x.dtype # np.dtype
x.size # int
y.index

#===== indexing, slicing, ... =====
x[:2] # simple but ambiguous
y.iloc[1] # different from y[1]

#===== calculation =====
x.sum()
x.mean()

#===== str accessor =====
y.str.len()
y.str.replace("\(.+\)", "")

#====================
# DataFrame
#====================

#===== prepare =====
x = pd.DataFrame({"salary": [100, 200, np.nan], "name": ["mickey", "donald", "goofy"]}, index=range(1, 4))
y = census[["area_code", "type", "value"]].copy() # deep copy
y["lvl"] = y["area_code"].str.len()
y.set_index(["area_code", "type"], inplace=True)
z = pd.DataFrame({"value":range(9)}, index=pd.date_range("2018-08-01", "2018-08-05", freq="12H"))
a = y.query("type == '人口総数'").copy()
b = y.query("type == '世帯総数'").copy()
c = y.query("lvl == 5").copy()

#===== attributes =====
x.values # ndarray
x.columns
x.index
y.index.get_level_values("area_code") # int is also available
y.index.names

#===== transform =====
#=== basic
x.T
y.unstack("type") # level
y.unstack("type").stack()

#=== index
y.reset_index("type") # index -> column
y.reset_index("type").set_index("type", append=True) # column -> index

#===== concat, merge, ... =====

#=== concat
pd.concat([x, x])
pd.concat([x, x], axis=1)

#=== merge
pd.merge(a, b, on="area_code") # inner join
pd.merge(a, b, on="area_code", how="left") # left join
pd.merge(a, b, on="area_code", how="outer")# full join
pd.merge(a, b, left_on="area_code", right_on="area_code")
# column name is also available

#===== indexing, slicing, ...  =====
#=== Series
y["value"]
y[["value", "lvl"]]

#=== conditional expression
y[y["lvl"] == 5]
y.query("lvl == 5")

#=== label_location, integer_location
x.loc[1, :]
x.iloc[1, :]
#z.loc["2018", ] 

#=== MultiIndex
y.sort_index(inplace=True) # important!
y.loc[("15101", "人口総数"), :]

#===== calculation =====
#=== basic
a.max()
a.describe() # summary

#=== group by
c.groupby(["type"]).mean()["value"]
c.groupby(["type"]).aggregate([np.mean, np.median])["value"]

c.groupby(["type"]).filter(lambda x: x["value"].min() > 300)
# having clause of SQL, but the return is each record
# function must return boolean

c.groupby(["type"]).transform(lambda x: x - x.mean())["value"] # centuring

#=== pivot
pd.pivot_table(y, index="area_code", columns="type", aggfunc=np.sum)
# both column and level of the index seem available

#===== time, datetime, ... =====
#=== DatetimeIndex
pd.to_datetime(["2015-01-01","2016-01-01"])
pd.to_datetime(["2015年01月01日","2016年01月01日"],format="%Y年%m月%d日")

#=== resample (more useful than asfreq)
z.resample("D").mean()["value"]
z.reset_index().resample("D", on="index").mean() # column is also available

#===== nan =====
#=== detect
x.isnull()
x.isnull().sum()

#=== remove
x.dropna()

#=== fill
x.fillna(0)
