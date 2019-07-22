from config import create_api
import logging
import time
import tweepy

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        
        new_since_id = max(tweet.id, new_since_id)
        if tweet.text is not None:
            if all(keyword in tweet.text.lower() for keyword in keywords):
                
                #follow and favorite tweet if not already
                if not tweet.user.following:
                    tweet.user.follow()
                    tweet.favorite()
                    
                api.update_status(status="YOU'RE breathtaking!",
                                  in_reply_to_status_id=tweet.id)
                
    return new_since_id

def main():
    
    api = create_api()
    since_id = 1
    print(since_id)
    since_id = check_mentions(api, ["you're", "breathtaking"], since_id)

if __name__ == "__main__":
    main()