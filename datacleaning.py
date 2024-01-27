import pandas as pd 
import ast 


def data_split(dataset): 
    data= pd.read_csv(dataset)
    columns = ["Date", "Comment"]
    new_df = data[columns].copy()
    # Convert the] string representation of the list to an actual list using ast.literal_eval
    new_df['Comment'] = new_df['Comment'].apply(ast.literal_eval)
    df_expanded = new_df.explode('Comment')
    df_expanded.to_csv(f'{dataset}_split.csv')
    return df_expanded

data_split('reddit_data.csv')
data_split('terrorist_reddit_data.csv')
data_split('war_reddit_data.csv')
data_split('Jenin_reddit_data.csv')
data_split('ISIS_reddit_data.csv')

# for name in dataset_names: 
#     data = pd.read_csv(f'name.csv')
#     columns = ["Date", "Comment"]
#     new_df = data[columns].copy()
#     # Convert the] string representation of the list to an actual list using ast.literal_eval
#     new_df['Comment'] = new_df['Comment'].apply(ast.literal_eval)

# # Explode the list of comments into separate rows
# df_expanded = new_df.explode('Comment')
# data = pd.read_csv('reddit_data.csv')
# print(data.head())
# print(data.columns)
# #print(data['Date'])
# print(list(data['Comment']))
# columns = ["Date", "Comment"]
# new_df = data[columns].copy()
# # Convert the] string representation of the list to an actual list using ast.literal_eval
# new_df['Comment'] = new_df['Comment'].apply(ast.literal_eval)

# # Explode the list of comments into separate rows
# df_expanded = new_df.explode('Comment')

# # Display the reshaped DataFrame
# print(df_expanded)
# df_expanded()