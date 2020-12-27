# imports pandas lib
import pandas as pd

# reads in data set as txt file with index column of user_id and separator as |
user = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', index_col="user_id",
                   sep="|")

# prints top 25 rows
print(user.head(25))

# prints bottom 10 rows
print(user.tail(10))

# prints result count and number of columns
print(user.shape)

# prints number of columns
print(user.shape[1])

# prints name of columns
print(user.columns)

# prints indices
print(user.index)

# prints datatype for each column
print(user.dtypes)

# prints occupation column
# print(user['occupation']) #same result but below is better
print(user.occupation)

# prints unique occupation
print(user.occupation.nunique())
print(user.occupation.value_counts())

# prints most frequent occupation
print(user.occupation.value_counts().head(1).index[0])

# prints summary of dataset
print(user.describe())

# prints summary of columns
print(user.describe(include='all'))

# prints summary of occupation
print(user.occupation.describe())

# prints mean age
print(user.age.mean())

# print last item
print(user.age.tail(1))
# print least frequent age

print(user.age.value_counts().tail())
