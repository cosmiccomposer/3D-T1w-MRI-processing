import numpy as np
import pandas as pd

data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]
df = pd.DataFrame(data, columns=columns)
df
# we can use a list of dictionaries to create a dataframe: 
data = [
    {
        "Make": "Nissan",
        "Model": "Stanza",
        "Year": 1991,
        "Engine HP": 138.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "sedan",
        "MSRP": 2000
    },
    {
        "Make": "Hyundai",
        "Model": "Sonata",
        "Year": 2017,
        "Engine HP": None,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "Sedan",
        "MSRP": 27150
    },
    {
        "Make": "Lotus",
        "Model": "Elise",
        "Year": 2010,
        "Engine HP": 218.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "convertible",
        "MSRP": 54990
    },
    {
        "Make": "GMC",
        "Model": "Acadia",
        "Year": 2017,
        "Engine HP": 194.0,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "4dr SUV",
        "MSRP": 34450
    },
    {
        "Make": "Nissan",
        "Model": "Frontier",
        "Year": 2017,
        "Engine HP": 261.0,
        "Engine Cylinders": 6,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "Pickup",
        "MSRP": 32340
    }
]
df = pd.DataFrame(data)
df
df.head(n=2)
#Series- Columns in a data frame - series. To access it, use dot or brackets
df.Make
df['Make']
#If a name contains spaces, we can't use dot, only brackets
df['Engine HP']

col_name = 'Engine HP'
df[col_name]

#use a list to select a subset of columns
df[['Make', 'Model', 'MSRP']]

#adding changes, removing columns
df['id'] = ['nis1', 'hyu1', 'lot2', 'gmc1', 'nis2']
df
df['id'] = [1, 2, 3, 4, 5]
df

del df['id']
df

#Indexing
df.index
df.Make.index 
df.columns

#accessing rows and shuffling
df.iloc[0]
df.iloc[[2, 3, 0]]

idx = np.arange(5)
idx

np.random.seed(2)
np.random.shuffle(idx)
idx
df.iloc[idx]
df

df.iloc[[0,1,2]]
df.index

df.loc[[0, 1]]
df.iloc[[0, 1]]
df
df.reset_index(drop=True)

#splitting the data 
n_train = 3
n_val = 1
n_test = 1

df_train = df.iloc[:n_train]
df_val = df.iloc[n_train:n_train+n_val]
df_test = df.iloc[n_train+n_val:]

df[['Make', 'Model', 'Year']]

df_train[['Make', 'Model', 'Year']]

df_val[['Make', 'Model', 'Year']]

df_test[['Make', 'Model', 'Year']]
df
df.reset_index(drop=True)

df.reset_index(drop=True)
df

#Element Operations
df['Engine HP']
df['Engine HP'] *2
df['Year']
df['Year'] >2000
df['Make'] == 'Nissan'

df['Year'] > 2000) & (df['Make'] == 'Nissan')

#Filtering
df[df['Make'] == 'Nissan']
df[(df['Year'] > 2010) & (df['Transmission Type'] == 'AUTOMATIC')]


#string operations
df['Vehicle_Style']
df['Vehicle_Style'].str.lower()

df['Vehicle_Style'].str.replace(' ', '_')

df['Vehicle_Style'].str.lower().str.replace(' ', '_')

df.columns

df.columns.str.lower().str.replace(' ', '_')

df.columns = df.columns.str.lower().str.replace(' ', '_')
df
df.dtypes

df.dtypes.index
df.dtypes == 'object'

df.dtypes[df.dtypes == 'object']

df.dtypes[df.dtypes == 'object'].index

list(df.dtypes[df.dtypes == 'object'].index)

string_columns = df.dtypes[df.dtypes == 'object'].index

for col in string_columns:
    df[col] = df[col].str.lower().str.replace(' ', '_')
df

#summarizing operations (EDA)
df.msrp
df.msrp.mean()

df.msrp.sum()
df.msrp.min(), df.msrp.max(), df.msrp.mean(), df.msrp.std()
#show operations
df.msrp.describe()
df.mean()
df.describe().round(2)
#catagorical columns
df.make.nunique()
df.nunique()
df.make.value_counts


#identify Missing values
df
df.isnull()

df.isnull().sum()
df.engine_hp.isnull()
df.engine_hp.fillna(0)
df.engine_hp.fillna(df.engine_hp.mean())
df.engine_hp = df.engine_hp.fillna(df.engine_hp.mean())
df

#sorting and reordering
df
df.sort)values(by='msrp')
df.sort)values(by='msrp', ascending=False)

#grouping
df.groupby('transmission_type').msrp.mean()
df.groupby('transmission_type').msrp.agg(['mean', 'count'])

df.groupby('transmission_type').msrp.agg(['mean', 'count'])
df_group

df_group['mean'] - df.msrp.mean()

#Accessing the Numpy Array
df.msrp
np.log1p(df.msrp)
df.msrp.values
np.log1p(df.msrp.values)

#Conversion to Dictionary

df.to_dict(orient='rows')
