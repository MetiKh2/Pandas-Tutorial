import pandas as pd

a=[3,7,2]

calories={'day1':420,'day2':380,'day3':390}
data={
    'calories':[420,380,390],
    'duration':[50,40,45]
}

myvar=pd.Series(a,index=['x','y','z'])
myvar=pd.Series(calories,index=['day1','day3'])
myvar=pd.DataFrame(data)

print(myvar)
# print(myvar['y']) 
