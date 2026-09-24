import pandas as pd,os

data={'name':['Alice','Cooper','Trevor'],
    'age':[21,32,29],
    'City':['New York','LA','Chicago']}

df=pd.DataFrame(data)

#adding new row
new_row1 ={'name':'new1','age':34,'City':'city1'}
df.loc[len(df.index)]=new_row1

dir_name='data'
os.makedirs(dir_name,exist_ok=True)

file_name=os.path.join(dir_name,'sample_data.csv')

df.to_csv(file_name,index=False)




