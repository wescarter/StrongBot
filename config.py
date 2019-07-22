import logging
import os
import tweepy

logger = logging.getLogger()

#set file path to upload OAUTH keys
os_path   = "D:/evnca/projects/StrongBot/"
os_root   = "authkeys.txt"
file_path = os.path.join(os_path+os_root)

def create_api():

    #read in auth file contents
    auth_table = {}
    auth_file  = open(file_path, 'r')
    for line in auth_file:
            
        key, *values = line.rstrip('\n').split(':')
        auth_table[key] = [value for value in values]
    
    auth_file.close()

    consumer_key        = str(auth_table['CONSUMER_KEY']).strip("'[]'")
    consumer_secret     = str(auth_table['CONSUMER_SECRET']).strip("'[]'")
    access_token        = str(auth_table['ACCESS_TOKEN']).strip("'[]'")
    access_token_secret = str(auth_table['ACCESS_TOKEN_SECRET']).strip("'[]'")

    #attempt to authenticate credentials   
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True,
                     wait_on_rate_limit_notify = True)

    logger.info("Authenticating...")
    try:
        api.verify_credentials()
        print("Authentication successful")

    except Exception as e:
        
        logger.error("Error creating API: Check credentials.", exc_info=True)
        raise e

    logger.info("API creation successful.")
    return api