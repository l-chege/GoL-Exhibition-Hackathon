consumer_secret = ''
access_token = '
access_token_secret = ''
auth = tw.OAuthHandler(consumer_key, consumer_secret) auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

user = api.me()
print('User details are: ')
print(user.name)
print(user.screen_name)
print(user.followers_count)

for friend in user. friends():
    print(friend.screen_name)
   
for follower in tw. Cursor(api.followers).items():
    follower.follow()


