import pandas

df = pandas.read_csv('hrdata.csv', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
           names=['Employee', 'Hired','Salary', 'Sick Days'])
print(df)
