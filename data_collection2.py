import pandas as pd 
import praw 
import datetime

reddit = praw.Reddit(
    client_id="LjLEdCZgjuDL-NW7rlVxhA",
    client_secret="Uu3aoj_tBfzvCE3LMwOnP1A3q9EsYQ",
    user_agent="Status_Huckleberry89 "
)

def get_reddit_data(search_query, subreddit_name, post_num, comment_num):
    subreddit = {}
    title = {}
    flair = {}
    date = {}
    body = {}
    comments = {}
    i = 1
    search_results = reddit.subreddit(subreddit_name).search(search_query, sort="relevance", limit=post_num)
    for submission in search_results:
        subreddit[i] = submission.subreddit.display_name
        title[i] = submission.title
        flair[i] = submission.link_flair_text
        date[i] = datetime.datetime.utcfromtimestamp(submission.created_utc).strftime('%d/%m/%Y %H:%M:%S')
        body[i] = submission.selftext
        top_comments = submission.comments.list()[:comment_num]
        ci = []
        for comment in top_comments:
            ci.append(comment.body)
        comments[i] = ci
        i+=1
    return subreddit, title, flair, date, body, comments

general_subreddits = {}
general_titles = {}
general_flairs = {}
general_dates = {}
general_bodies = {}
general_comments = {}
general_subreddits["Jenin"], general_titles["Jenin"], general_flairs["Jenin"], general_dates["Jenin"], general_bodies["Jenin"], general_comments["Jenin"] = get_reddit_data("Jenin", "IsraelWar", 20, 10)

data = {
    'Subreddit': general_subreddits["Jenin"],
    'Title': general_titles["Jenin"],
    'Flair': general_flairs["Jenin"],
    'Date': general_dates["Jenin"],
    'Body': general_bodies["Jenin"],
    'Comment': general_comments["Jenin"]
}

Jenin_reddit_df = pd.DataFrame(data)

# Display the DataFrame
print(Jenin_reddit_df.head())

# Save the DataFrame to a CSV file
Jenin_reddit_df.to_csv('Israelwar.csv', index=False)