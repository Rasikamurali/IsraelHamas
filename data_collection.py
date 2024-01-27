import pandas as pd 
import praw 
from datetime import datetime

reddit = praw.Reddit(
    client_id="LjLEdCZgjuDL-NW7rlVxhA",
    client_secret="Uu3aoj_tBfzvCE3LMwOnP1A3q9EsYQ",
    user_agent="Status_Huckleberry89 "
)



subreddit = reddit.subreddit("Israelcrimes")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

posts = subreddit.top("year")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [], "Post URL": []
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	
	# URL of each post
	posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts.head())
print(len(top_posts))

from praw.models import MoreComments
p_urls = list(top_posts['Post URL'])
post_comments = []
post_dates = []
#Creating a submission object
for url in p_urls:
    try:
        submission = reddit.submission(url=url)
        submission.comments.replace_more(limit=None)  # This line fetches all comments, including MoreComments

        for comment in submission.comments.list():
            post_comments.append(comment.body)
            post_dates.append(datetime.fromtimestamp(comment.created_utc))

    except Exception as e:
        print(f"Error processing URL {url}: {e}")

# Creating a dataframe
comments_df = pd.DataFrame({'comment': post_comments, 'post_dates': post_dates})
print(comments_df.head())

# Writing to CSV file
try:
    comments_df.to_csv('IsraelCrimescomments.csv', index=False)  # Set index=False to avoid writing row indices to the CSV file
    print("Data successfully written to comments.csv")
except Exception as e:
    print(f"Error writing to CSV file: {e}")

# submission = reddit.submission(url = p_urls[0])
# for comment in submission.comments:
#         if type(comment) == MoreComments:
#             continue

#         post_comments.append(comment.body)
#         print(datetime.fromtimestamp(comment.created_utc))
    

# # creating a dataframe
# comments_df = pd.DataFrame(post_comments, columns=['comment'])
# print(comments_df.head())
