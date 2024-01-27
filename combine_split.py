import pandas as pd 
import datetime 

df1 = pd.read_csv('IsraelPalestinecomments.csv')
df2 = pd.read_csv('IsraelCrimescomments.csv')
df3 = pd.read_csv('IsraelWarcomments.csv')
df4 = pd.read_csv('HamasWarcomments.csv')
df5 = pd.read_csv('reddit_data.csv_split.csv')
df6 = pd.read_csv('war_reddit_data.csv_split.csv')
df7 = pd.read_csv('terrorist_reddit_data.csv_split.csv')
df8 = pd.read_csv('ISIS_reddit_data.csv_split.csv')
df9 = pd.read_csv('Jenin_reddit_data.csv_split.csv')

merged_df = pd.concat([df1, df2, df3, df4]) 
merged_df2 = pd.concat([df5, df6, df7, df8, df9])
print(merged_df.head())

merged_df2['Date'] = pd.to_datetime(merged_df2['Date'], format='%d/%m/%Y %H:%M:%S').dt.strftime('%Y-%m-%d %H:%M:%S')
# Swap the entire 'Value1' and 'Value2' columns
temp_column = merged_df2['Date'].copy()

merged_df2 = merged_df2.drop(columns=['Date'])
merged_df2['Date'] = temp_column
# Display the modified DataFrame

print(merged_df2.head())
merged_df2.rename(columns={'Comment': 'comment', 'Date': 'post_dates'}, inplace=True)


merged_df3 = pd.concat([merged_df, merged_df2])
print(merged_df3.head())
merged_df3['post_dates'] = pd.to_datetime(merged_df3['post_dates'], format='%Y-%m-%d %H:%M:%S', errors='coerce')


# Define date ranges
start_date1 = pd.to_datetime('07/10/2023', format='%d/%m/%Y')
end_date1 = pd.to_datetime('14/10/2023', format='%d/%m/%Y')

start_date2 = pd.to_datetime('10/11/2023', format='%d/%m/%Y')
end_date2 = pd.to_datetime('17/11/2023', format='%d/%m/%Y')

start_date3 = pd.to_datetime('09/06/2023', format='%d/%m/%Y')
end_date3 = pd.to_datetime('06/10/2023', format='%d/%m/%Y')

start_date4 = pd.to_datetime('26/01/2023', format='%d/%m/%Y')
end_date4 = pd.to_datetime('02/02/2023', format='%d/%m/%Y')

start_date5 = pd.to_datetime('17/01/2023', format='%d/%m/%Y')
end_date5 = pd.to_datetime('25/01/2023', format='%d/%m/%Y')

start_date6 = pd.to_datetime('02/02/2023', format='%d/%m/%Y')
end_date6 = pd.to_datetime('09/02/2023', format='%d/%m/%Y')


# Split the DataFrame based on date ranges#
#df_range1 = merged_df3[(merged_df3['post_dates'] >= pd.to_datetime(start_date1, format='%d/%m/%Y %H:%M:%S')) & (merged_df3['post_dates'] < pd.to_datetime(end_date1, format='%d/%m/%Y %H:%M:%S'))]
#df_range2 = merged_df3[(merged_df3['post_dates'] >= start_date2) & (merged_df3['post_dates'] < end_date2)]
df_range3 = merged_df3[(merged_df3['post_dates'] >= pd.to_datetime(start_date6, format='%d/%m/%Y %H:%M:%S')) & (merged_df3['post_dates'] < pd.to_datetime(end_date6, format='%d/%m/%Y %H:%M:%S'))]
#df_range1.to_csv('during_hamas.csv')
#df_range2.to_csv('post_hamas.csv')
df_range3.to_csv('before_jenin.csv')