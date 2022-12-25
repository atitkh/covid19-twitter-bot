import tweepy
import logging
import time
import random
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

from config import create_api
api = create_api()

def fav_retweet(api):
    logger.info('Retrieving tweets...')
    mentions = api.mentions_timeline(tweet_mode='extended')
    for mention in reversed(mentions):
        if mention.in_reply_to_status_id is not None or mention.user.id == api.me().id:
            # This tweet is a reply or I'm its author so, ignore it
            return

        if not mention.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                mention.favorite()
                logger.info(f"Liked tweet by {mention.user.name}")
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

        if not mention.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                mention.retweet()
                logger.info(f"Retweeted tweet by {mention.user.name}")
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)


def fav_retweet_user(api, user_handle):
    search_query = f"{user_handle} -filter:retweets"
    logger.info(f'Retrieving tweets mentioning {user_handle}...')
    tweets = api.search(q=search_query, lang ="en")
    for tweet in tweets:
        if tweet.in_reply_to_status_id is not None or tweet.user.id == api.me().id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                logger.info(f"Liked a tweet mentioning {user_handle}")
            except Exception as e:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                logger.info(f"Retweeted a tweet mentioning {user_handle}")
            except Exception as e:
                logger.error("Error on fav and retweet", exc_info=True)


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                follower.follow()
                logger.info(f"Following {follower.name}")
                time.sleep(5)
            except tweepy.error.TweepError:
                pass

def unfollow_unfollowers(api):
    for friend in tweepy.Cursor(api.friends).items():
        if friend not in tweepy.Cursor(api.followers).items():
                logger.info('Unfollowing @%s (%d)',
                friend.screen_name, friend.id)
                try:
                    api.destroy_friendship(friend.id)
                    time.sleep(5)
                except tweepy.error.TweepError:
                    logger.exception('Error unfollowing.')


def retweet_tweets_with_hashtag(api, user_handle):
    return


def tweet_daily(api, last_tweeted, text):
    if last_tweeted < datetime.now()-timedelta(hours=24):
        api.update_status(text)
        logger.info(f"Tweeted {text} at {datetime.now().strftime('%m/%d/%Y at %H:%M:%S')}")
        return datetime.now()
    else:
        return last_tweeted


def run_in(api, last_run, hrs):
    if last_run < datetime.now()-timedelta(hours=hrs):
        #code to run
        logger.info(f"Running Scheduled Code..")
        return datetime.now()
    else:
        return last_run

# Retweet the keywords in trend
def trend_retweet(api):
    trendsPlace = api.trends_place(23424977) # id for Worldwide, view more here: https://codebeautify.org/jsonviewer/f83352
    data = trendsPlace[0]
    trends = data['trends']
    # Get the name from each trend
    names = [trend['name'] for trend in trends]
    count = 0
    for name in names:
        #print(names)
        for tweet in tweepy.Cursor(api.search, name, result_type='popular').items(1):
            try:
                if (not tweet.retweeted) and ('RT @' not in tweet.text) and count < 2: # This is to prevent dupicating retweets
                    print(name)
                    tweet.retweet()
                    tweet.favorite()
                    print('Retweeted the tweet.')
                    count = count + 1
                    time.sleep(10) # Sleep for 10seconds so we will not be banned by Twitter
                else:
                    break
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break


def tweet(text):
    api.update_status(status=text)
