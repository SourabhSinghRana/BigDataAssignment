



Q1. To load a CSV file into a Pandas DataFrame, you can use the read_csv() function in Pandas:

import pandas as pd
df = pd.read_csv('file.csv')




Q2. To check the data type of a column in a Pandas DataFrame, you can use the dtype attribute:

print(df['column_name'].dtype)




Q3. To select rows from a Pandas DataFrame based on a condition, you can use boolean indexing:

new_df = df[df['column_name'] > 5]




Q4. To rename columns in a Pandas DataFrame, you can use the rename() method:

df = df.rename(columns={'old_name': 'new_name'})




Q5. To drop columns in a Pandas DataFrame, you can use the drop() method:

df = df.drop(columns=['column_name1', 'column_name2'])




Q6. To find the unique values in a column of a Pandas DataFrame, you can use the unique() method:

unique_values = df['column_name'].unique()




Q7. To find the number of missing values in each column of a Pandas DataFrame, you can use the isnull() and sum() methods:

null_counts = df.isnull().sum()




Q8. To fill missing values in a Pandas DataFrame with a specific value, you can use the fillna() method:

df = df.fillna(value=0)




Q9. To concatenate two Pandas DataFrames, you can use the concat() function:

new_df = pd.concat([df1, df2], axis=0)




Q10. To merge two Pandas DataFrames on a specific column, you can use the merge() method:

new_df = pd.merge(df1, df2, on='column_name')




Q11. To group data in a Pandas DataFrame by a specific column and apply an aggregation function, you can use the groupby() method:

grouped_data = df.groupby('column_name').agg({'column_to_aggregate': 'sum'})




Q12. To pivot a Pandas DataFrame, you can use the pivot() method:

pivoted_df = df.pivot(index='index_column', columns='column_to_pivot', values='value_column')




Q13. To change the data type of a column in a Pandas DataFrame, you can use the astype() method:

df['column_name'] = df['column_name'].astype('new_data_type')




Q14. To sort a Pandas DataFrame by a specific column, you can use the sort_values() method:

sorted_df = df.sort_values('column_name', ascending=True)




Q15. To create a copy of a Pandas DataFrame, you can use the copy() method:

new_df = df.copy()




Q16. To filter rows of a Pandas DataFrame by multiple conditions, you can use boolean indexing with the & (and) or | (or) operators:

new_df = df[(df['column_name1'] > 5) & (df['column_name2'] == 'value')]




Q17. To calculate the mean of a column in a Pandas DataFrame, you can use the mean() method:

column_mean = df['column_name'].mean()




Q18. To calculate the standard deviation of a column in a Pandas DataFrame, you can use the std() method. For example, if you want to calculate the standard deviation of a column named 'column_name', you can use the following code:

df['column_name'].std()




Q19. To calculate the correlation between two columns in a Pandas DataFrame, you can use the corr() method. For example, if you want to calculate the correlation between columns 'column_1' and 'column_2', you can use the following code:

df['column_1'].corr(df['column_2'])




Q20. To select specific columns in a DataFrame using their labels, you can use the square bracket notation with a list of column labels. For example, if you want to select columns 'column_1' and 'column_2', you can use the following code:

df[['column_1', 'column_2']]




Q21. To select specific rows in a DataFrame using their indexes, you can use the loc[] method. For example, if you want to select rows with indexes 0, 1, and 2, you can use the following code:

df.loc[[0, 1, 2]]




Q22. To sort a DataFrame by a specific column, you can use the sort_values() method. For example, if you want to sort a DataFrame by column 'column_name' in ascending order, you can use the following code:

df.sort_values(by='column_name')




Q23. To create a new column in a DataFrame based on the values of another column, you can use the square bracket notation and assign the new column a list of values based on the existing column. For example, if you want to create a new column 'new_column' based on the values of an existing column 'column_name', you can use the following code:

df['new_column'] = [value * 2 for value in df['column_name']]




Q24. To remove duplicates from a DataFrame, you can use the drop_duplicates() method. For example, if you want to remove duplicates from column 'column_name', you can use the following code:

df.drop_duplicates(subset=['column_name'], keep='first', inplace=True)




Q25. The difference between .loc and .iloc in Pandas is that .loc is used to select data based on labels, while .iloc is used to select data based on integer positions. For example, if you want to select the first row of a DataFrame, you can use the following code:

df.iloc[0]
This will select the row based on its integer position. On the other hand, if you want to select the row with label 'label_1', you can use the following code:
df.loc['label_1']
This will select the row based on its label.