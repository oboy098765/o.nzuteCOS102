import pandas as pd
crypto = pd.read_csv("BTC_DATA_V3.0.csv")
apps = pd.read_csv("Top-Apps-in-Google-Play.csv")
programming = pd.read_csv("programming language trend over time.csv")

df1 = pd.DataFrame(crypto)
#Printing the first 7 rows
df1a = crypto.head(7)
print(df1a)
print()

#Printing the first 3 columns
columns1 = list(df1) 
print(df1[['Date', 'Price', 'Open']])
print()

#Printing only one row and header
df1b = crypto.head(1)
print(df1b)
print()
    

df2 = pd.DataFrame(apps)
#Printing the first 7 rows
df2a = apps.head(7)
print(df2a)
print()

#Printing the first 3 columns
columns2 = list(df2)
print(df2[['App Name', 'App Id', 'Category']])
print()

#Printing only one row and header
df2b = apps.head(1)
print(df2b)
print()
    

df3 = pd.DataFrame(programming)
#Printing the first 7 rows
df3a = programming.head(7)
print(df3a)
print()

#Printing the first three columns
columns3 = list(df3)
print(df3[['Week', 'Python', 'Java']])
print()

#Printing only one row and header
df3b = programming.head(1)
print(df3b)
print()
