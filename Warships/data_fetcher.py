# %%
import praw
import pandas as pd

# %%
client_id = 'redacted'
client_secret = 'redacted'
user_agent = 'redacted'

reddit = praw.Reddit(client_id = client_id,
                     client_secret = client_secret,
                     user_agent = user_agent)


WP = reddit.subreddit('WarshipPorn')

# %%
data = [submission.title for submission in WP.top('all', limit = 1000)]
data = pd.DataFrame({'title' : data})

# %%
data.to_csv('warships.csv', encoding =' utf-8')
