import logging
import os
import tweepy

logger = logging.getLogger()

#set file path to upload OAUTH keys
os_path   = "C:/Users/ecarter/projects/bots/StrongBot"
os_root   = "authkeys.txt"
file_path = os.path.join(os_path+os_root)

def create_api():
    #read in auth file contents
    auth_file = open(file_path, 'r')
    api_key       = auth_file.readline().rstrip('\n')
    api_token    = auth_file.readline().rstrip('\n')
    access_key    = auth_file.readline().rstrip('\n')
    access_token = auth_file.readline().rstrip('\n')
    auth_file.close()

    #attempt to authenticate credentials   
    auth = tweepy.OAuthHandler(api_key, api_token)
    auth.set_access_token(access_key, access_token)

    api = tweepy.API(auth, wait_on_rate_limit = True,
                     wait_on_rate_limit_notify = True)

    try:
        api.verify_credentials()
        print("Authentication is OK")

    except Exception as e:
        
        logger.error("Error creating API: Check credentials.", exc_info=True)
        raise e
    logger.info("API creation successful.")
    return api