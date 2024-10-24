import pandas as pd
df = pd.read_csv("sample1.csv")
print(df) # print all rows
print(df.tail(4)) # print last 4 rows
print("This is the the first row of the CSV")
print(df.head(1)) # print first row

print("slicing ")
print(df[2:6])

print("dataframe shape = ",df.shape)

print(df["year"])