import os
import tweepy

#set file path to upload OAUTH keys
os_path   = "C:/Users/ecarter/projects/bots/"
os_root   = "authkeys.txt"
file_path = os.path.join(os_path+os_root)

#read in auth file contents
auth_file = open(file_path, 'r')
api_key       = auth_file.readline().rstrip('\n')
api_secret    = auth_file.readline().rstrip('\n')
access_key    = auth_file.readline().rstrip('\n')
access_secret = auth_file.readline().rstrip('\n')
auth_file.close()

#authenticate to twitter   
auth_ok = False #auth ok flag
auth = tweepy.OAuthHandler(api_key,
                           api_secret)
auth.set_access_token(access_key,
                      access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True,
                 wait_on_rate_limit_notify = True)

try:
    
    api.verify_credentials()
    auth_ok = True
    print("Authentication is Go")

except:
    
    print("Authentication is NO-GO")