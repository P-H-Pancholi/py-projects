import pandas as pd

#pandas Series object works as a one-dimensional array
data = {'Month' : pd.Series(['January','February','March','April','May'
         , 'June', 'July', 'August', 'September','October','November', 
            'December']),
        'Rainfall' : pd.Series([1.65, 1.25, 1.94, 2.75, 2.75, 3.645, 5.5,
            1.0, 1.2, 1.3, 0.5, 2.3])} 
#DataFrame needs a dictionary of Series object


df = pd.DataFrame(data) #pandas DataFrame object looks like spreadsheet

dfc = pd.read_csv(r'./rain.csv') #using csv file

dfj = pd.read_json(r'./rain.json')#using json file

print("Our data frame:")
print(dfj,"\n")


#Remove rows with missing values
dfclean = dfj.dropna(0)
print("Our data after removing nan rows:\n",dfclean)

#fill the missing values with zeros

dfzeros = dfj.fillna(0)
print("Our data with zerod values  :\n",dfzeros) 

#count all rows that contains nan

count = 0
for index,row in dfj.iterrows():
    if any(row.isnull()):
        count += 1
print("The number of rows that contains nun is "+ str(count))
