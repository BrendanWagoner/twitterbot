import tweepy
import config
from spotify import get_tracks, bot_playlist_id


def create_tweet(message):
    client = tweepy.Client(consumer_key=config.api_key,
                           consumer_secret=config.secret_api,
                           access_token=config.access_token,
                           access_token_secret=config.access_secret)
    response = client.create_tweet(text=message)
    return response


def find_user(twitter_handle):
    client = tweepy.Client(bearer_token=config.bearer)
    user = client.get_user(username=twitter_handle)
    return user.data.id


def follow_user(twitter_handle):
    user_id = find_user(twitter_handle)
    client = tweepy.Client(consumer_key=config.api_key,
                           consumer_secret=config.secret_api,
                           access_token=config.access_token,
                           access_token_secret=config.access_secret)
    follow = client.follow_user(target_user_id=user_id, user_auth=True)
    return follow


user_ex = 'lmwbrendan'
# print(create_tweet(get_tracks(bot_playlist_id)))
print(get_tracks(bot_playlist_id))
# print(follow_user(user_ex))
