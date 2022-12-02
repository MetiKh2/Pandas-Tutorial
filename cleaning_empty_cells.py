import pandas as pd

df=pd.read_csv('data.csv')

mean=df['Calories'].mean()
median=df['Calories'].median()
mode=df['Calories'].mode()[0]
# df.dropna(inplace=True)
df['Calories'].fillna(mode,inplace=True)
print(df)
