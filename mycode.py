import pandas as pd,os

data={'name':['Alice','Cooper','Trevor'],
    'age':[21,32,29],
    'City':['New York','LA','Chicago']}

df=pd.DataFrame(data)

dir_name='data'
os.makedirs(dir_name,exist_ok=True)

file_name=os.path.join(dir_name,'sample_data.csv')

df.to_csv(file_name,index=False)

print('Data saved as csv file in directory')



