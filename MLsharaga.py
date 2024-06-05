import pandas as pd


adf = pd.read_csv(r'C:\Users\kliker\Desktop\anime_data.csv')
pd.set_option('display.max_columns', None)

print(adf.head(5))
#Delete column
adf.drop(['Members'], axis=1, inplace=True)


#Replace cell
adf.at[0, 'Name'] = 'GGGGG'
print(adf.head(5))


#Drop cell
adf.at[1, 'Name'] = None
print(adf.head(5))

#Sorted by
adf.sort_values(by='Score')
print(adf.head(5))



#Delete duplicates
adf.drop_duplicates(['Name'])
print(adf.head(5))

adf.to_csv(r'C:\Users\kliker\Desktop\new_anime_data.csv', sep='\t')