# step1:
- we can do simple data preprocessing steps; like converting the data into appropriate format, data column as the index

## file location : 

df1 = pd.read_csv('../../datasrc/NepseDataHistorical1997_2024.csv')   //copy and paste



step2: then we jump into EDA. 



## problems:
- the data form 2015 are showing nan
- i handel all the data in level 2 ;;;; df = pd.read_csv('../../datasrc/NepseDataHistorical1997_2024_sorted.csv')

## EDA1: 
- after solving the above data preprocessing in EDA1 i am covering the EDA process like: df.describe() for the statistical anlaysis 