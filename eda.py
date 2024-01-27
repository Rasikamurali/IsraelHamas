import pandas as pd 
from datetime import datetime as dt
from matplotlib import pyplot as plt 
import numpy as np 
import seaborn as sns

# print(len(data))
# print(data.head())
# # comments = (list(data['Comment']))
# # #print(comments[0])
# # single_comment = []
# # for comment in comments: 
# #     single_comment.append((comment.split("'")))
# dates = list(data["post_dates"])
# print(type(dates[0]))

# converted_dates = [] # Convert each date string to a datetime object
# date_objects = [dt.strptime(date_str, "%Y-%m-%d %H:%M:%S") for date_str in dates]

# # Find the maximum date
# max_date = max(date_objects)
# print(max_date)
# print(min(date_objects))
# # Display the maximum date
# print(max_date)

# print(min(list(data['Date'])))
# print(max(list(data['Date'])))
# print(type(list(data['Date'])[0]))

def average_emotions(data): 
    new_data = data.drop(columns=['Unnamed: 0', 'comment', 'post_dates'])
    columns = [] 
    for column in new_data.columns: 
        columns.append(column)
    print(columns)
    emotion_dict={}
    for column in columns: 
        emotion = list(data[column])
        emotion_dict[column] = np.average(emotion)
    plt.figure(figsize=(8, 10))
    plt.scatter(list(emotion_dict.keys()), list(emotion_dict.values()) )
    plt.title('avg emotion scores')
    plt.xlabel('Emotions')
    plt.ylabel('Emotion scores')
    plt.xticks(rotation = 90)
    plt.show()
    #plt.savefig(f'{data}_avg_emotion.png')

during_hammas = pd.read_csv('empath_during_hammas.csv')
#average_emotions(during_hammas)
post_hammas = pd.read_csv('empath_post_hammas.csv')
#average_emotions(post_hammas)

during_jenin = pd.read_csv('empath_during_jenin.csv')
#average_emotions(during_jenin)
post_jenin = pd.read_csv('empath_after_jenin.csv')
#average_emotions(post_jenin)

#I want a dataframe with the min, max and mean values for each emotion of the dataset 
def emotion_range(name, data):
    new_data = data.drop(columns=['Unnamed: 0', 'comment', 'post_dates'])
    columns = [] 
    for column in new_data.columns: 
        columns.append(column)
    print(columns)
    emotion_range = pd.DataFrame(columns=['emotion', 'min', 'max', 'median', 'mean'])

    for column in columns: 
        emotion = list(data[column])
        # Calculate the min, max, and median for the current emotion
        min_score = np.min(emotion)
        max_score = np.max(emotion)
        median_score = np.median(emotion)
        mean_score = np.mean(emotion)
        # Append the results to the emotion_range DataFrame
        emotion_range = emotion_range._append({
            'emotion': column,
            'min': min_score,
            'max': max_score,
            'median': median_score, 
            'mean': mean_score
        }, ignore_index=True)

    print(emotion_range.head())
    emotion_range.to_csv(f'{name}_summarystats.csv')

#         summary_stats.boxplot()

emotion_range('during_hammas', during_hammas)
emotion_range('post_hammas', post_hammas)
emotion_range('during_jenin', during_jenin)
emotion_range('post_jenin', post_jenin)

def box_plots(name, data): 
    new_data = data.drop(columns=['Unnamed: 0', 'comment', 'post_dates'])

        # Melt the DataFrame to long format for boxplot
    melted_data = pd.melt(new_data, var_name='emotion', value_name='score')

        # Create a boxplot using seaborn
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='emotion', y='score', data=melted_data)
    plt.title(f'Boxplot of Emotion Scores for {name}')
    plt.show()

box_plots('during_hammas', during_hammas)
box_plots('post_hammas', post_hammas)
box_plots('during_jenin', during_jenin)
box_plots('post_jenin', post_jenin)