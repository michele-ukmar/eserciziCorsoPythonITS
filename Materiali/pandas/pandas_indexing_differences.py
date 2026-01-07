import pandas as pd
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)

print(df[1:4][['A','C']])
#    A   C
# 1  2  12
# 2  3  13
# 3  4  14

print(df.iloc[1:4,[0,2]])
#    A   C
# 1  2  12
# 2  3  13
# 3  4  14

print(df.loc[1:3,['A','C']])
#    A   C
# 1  2  12
# 2  3  13
# 3  4  14