import pandas as pd
from empath import Empath

data = pd.read_csv('after_jenin.csv')
print(data.head())

# Perform Empath sentiment analysis
lexicon = Empath()
sentiments = []

comments = list(data['comment'])
sentiments = [] 
for comment in comments: 
    sentiment = lexicon.analyze(comment, normalize=True)
    #print(sentiment)
    sentiments.append(sentiment)

print(sentiments[0])
sentiments_df = pd.DataFrame(sentiments)
full_df = pd.concat([data, sentiments_df], axis=1)

print(sentiments_df.head())
print(full_df.head())

# Reshape DataFrame to have 'Emotion' and 'Counts' columns
melted_df = pd.melt(sentiments_df, var_name='Emotion', value_name='Counts')

# Group by 'Emotion' and sum the counts
emotions_counts = melted_df.groupby('Emotion')['Counts'].sum().reset_index()

# Pick the top 10 emotions based on counts
top_10_emotions = emotions_counts.nlargest(10, 'Counts')

print("Top 10 Emotions:")
print(top_10_emotions)

print(full_df.head())
columns = [] 
for emotion in list(top_10_emotions['Emotion']): 
    columns.append(emotion)
    
columns += ['comment', 'post_dates']  # Add 'comment' and 'date' to the columns list

# Select the columns in final_df
final_df = full_df[columns]
print(final_df.head())
final_df.to_csv('empath_after_jenin.csv')

#top_10_df = full_df[full_df['Emotion'].isin(top_10_emotions['Emotion'])]


# # Create a DataFrame with column names and counts of non-zero values for each column
# non_zero_counts = sentiments_df.apply(lambda col: (col.name, col[col != 0].count()), axis=0)

# # Display the column names and counts
# print(non_zero_counts)
# non_zero_counts_df = pd.DataFrame(non_zero_counts, columns=['Column', 'Non-Zero Counts'])
# #non_zero_counts_df.to_csv('empath_columns.csv')


# # Add an index column to make 'Column' values unique
# non_zero_counts_df['Index'] = range(len(non_zero_counts_df))

# # Pivot the DataFrame using pivot_table
# pivoted_counts_df = non_zero_counts_df.pivot_table(index='Index', columns='Column', values='Non-Zero Counts', aggfunc='first')

# # Drop the 'Index' column after the pivot
# pivoted_counts_df = pivoted_counts_df.droplevel(0, axis=1)

# # Display the pivoted DataFrame
# print(pivoted_counts_df)

