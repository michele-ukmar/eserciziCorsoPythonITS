
import pandas as pd

adult  = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", \
                     names = ['age','workclass','fnlwgt', 'education','education_num','marital_status','occupation',\
                              'relationship','race','sex','capital_gain','capital_loss', 'hours_per_week', 'native_country','label'],\
                     index_col = False)

print("Shape of data{}".format(adult.shape))
print(adult.head())

print(adult.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 32561 entries, 0 to 32560
# Data columns (total 15 columns):
#  #   Column          Non-Null Count  Dtype 
# ---  ------          --------------  ----- 
#  0   age             32561 non-null  int64 
#  1   workclass       32561 non-null  object
#  2   fnlwgt          32561 non-null  int64 
#  3   education       32561 non-null  object
#  4   education_num   32561 non-null  int64 
#  5   marital_status  32561 non-null  object
#  6   occupation      32561 non-null  object
#  7   relationship    32561 non-null  object
#  8   race            32561 non-null  object
#  9   sex             32561 non-null  object
#  10  capital_gain    32561 non-null  int64 
#  11  capital_loss    32561 non-null  int64 
#  12  hours_per_week  32561 non-null  int64 
#  13  native_country  32561 non-null  object
#  14  label           32561 non-null  object
# dtypes: int64(6), object(9)
# memory usage: 3.7+ MB
# None

adult.index.name = 'adult_index'

print(adult.index.name)

print(adult[1:10])