# %%
import tweepy
import traceback
import pandas as pd
import keys as k

# %%
auth = tweepy.OAuthHandler(k.CONSUMER_KEY, k.CONSUMER_SECRET)
auth.set_access_token(k.ACCESS_TOKEN, k.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# %%
def user_timeline(user_id,tweet_limit):
    """
    Get tweets of user
    """
    try:
        pages_count = int(tweet_limit)/k.TWEETS_PER_PAGE
        new_tweets = tweepy.Cursor(api.user_timeline,screen_name=user_id).pages(pages_count)
        return new_tweets
    except tweepy.TweepError as err:
        raise Exception(traceback.format_exc())
# %%
def fetch_twitter_account_posts(user_id,limit):
    all_tweets = []
    page_cursor = user_timeline(user_id, limit)
    for page in page_cursor:
        for tweet in page:
            all_tweets.append(tweet._json)
    return pd.DataFrame(all_tweets)
# %%
latest_tweets = fetch_twitter_account_posts('elonmusk',100)
# %%
latest_tweets.to_excel("tmp/edata.xlsx")
# %%
