# ******* Panda *******
# Panda is powreful python data analytics library
# The library provids high-performance, easy-to-use data structure and data analysis and modeling tools that is fast and flexible
# it uses "relational" or "labeled" data both easy and intuitive
# it is rounding up the capabilities of Numpy, Scipy and Matplotlib

# data structure :
   # Series : A series is a one dimensional labelled array-like object
   # DataFrame : DataFrame is based on spreadsheets concepts

# ******* Panda Series *******

import pandas as pd
data = [100,120,140,180,200,210,214]
s = pd.Series(data)
print(s.describe())
s.plot(kind="bar")

#####################################

print(s)
s.index = ["a", "b", "c", "d", "e", "f", "g"]
print(s)
print("mean : ",s.mean())
print("std : ",s.std())
print(s.agg(("sum","max")))
s.plot()

# ******* DataFrame *******

dict = {"country" : ["Brasil","Russia","India", "China","South Africa"],
        "Capital" : ["Brasilla","Moscow","New Dehli","Beijing","Pretoria"],
        "Area"    : [8.516,17.10,3.386,9.597,1.221],
        "population" : [200.4,143.5,1252,1357,52.98]}
my_data = pd.DataFrame(dict)
print("mean : ", my_data.mean())
print(my_data.describe())
my_data.index = ["BR","RU","IN","CH","SA"]
print(my_data)

#####################################

d = {"one" : [1,2,3,4,5],
     "two" : [2,2,2,2,2],
     "letter" : ["a","a","b","b","c"]}
df = pd.DataFrame(d)
for index, row in df.iterrows():
    print(row['two']+3, row['letter'])

#####################################

names = ["Bob","Jessica","Mary","John","Mel"]
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print(BabyDataSet)
df = pd.DataFrame(data=BabyDataSet, columns = ["Names","Births"])
print(df)
df = df.sort_values(["Births"],ascending=False)
print(df)
print(df.head())
print("Max Births :", df["Births"].max)
print("Sum Births :", df["Births"].sum())

# ******* Appling functions on data *******

import numpy as np
d = {"one" : [1,2,3,4,5],
     "two" : [2,2,2,2,2],
     "letter" : ["a","a","b","b","c"]}
df = pd.DataFrame(d)
print(df)
print(df['one'].apply(np.sqrt))
print(df["letter"].map(lambda x :'map_'+ x))

# ******* DataFrame-adding/deleting columns *******

c = [0,1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(c)
print(df)
df.columns = ['Rev']
df['NewCol'] = 5
print(df)
del df['NewCol']
print(df)
df["test"] = 3
df["col"] = df["Rev"]
print(df)
i = ["a","b","c","d","e","f","g","h","i","j"]
df.index = i
print(df)
print(df.loc['a'])
print(df.loc['a':'d'])
print(df.iloc[0:3])
print(df[["Rev","test"]])
print(df.head())
print(df.tail(3))

# ******* DataFrame-GroupBy *******

e = {"one" : [1,2,3,4,5],
     "two" : [2,2,2,2,2],
     "letter" : ["a","a","b","b","c"]}
df = pd.DataFrame(e)
print(df)
gdf = df.groupby('letter')
print(gdf.sum())
letterone = df.groupby(["letter","one"]).sum()
print(letterone)

# ******* Export to excel and csv formats *******

f = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(f, columns = ["Number"])
df.to_excel("PandaText.xlsx",sheet_name = "testing", index=True)
df.to_csv("myDataFrame.csv",sep="\t")

# ******* Reading from files ******

df = pd.read_csv("myDataFrame.csv", sep='\t', index_col=0)
print(df)

# ******* Plotting ******

j = {"one" : [10,20,5,40,70,10,20,5,40,70],
     "two" : [14,0,30,40,20,14,0,70,40,20]}
df = pd.DataFrame(j, columns=["one","two"])
df.plot()

#####################################

fruits1 = ["apples", "pears", "cherries", "bananas"]
series1 = pd.Series([10,30,50,10],
                   index = fruits1,
                   name = 'series')
print(series1)
series1.plot.pie(figsize=(6,6))

#####################################

fruits2 = ["apples", "pears", "cherries", "bananas"]
series2 = pd.Series([10,30,50,10],
                   index = fruits2,
                   name = 'series')
print(series2)
explode = [0,0.10,0.40,0.7]
series2.plot.pie(figsize=(6,6),explode=explode)
