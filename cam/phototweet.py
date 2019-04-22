import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def postTweets(photos, message):
    photo_path = '/home/pi/ttr/Projects/Python/spycam/' + photos
    photo_path1 = '/home/pi/ttr/Projects/Python/spycam/img(1).jpg'
    status = message

    api.update_with_media(photo_path, status=status)
