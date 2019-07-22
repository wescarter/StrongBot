from config import create_api
import logging
import time
import tweepy

def check_mentions(api, keywords, since_id):
    
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            if tweet.text.lower() == "you're breathtaking!":
                
                if not tweet.user.following:
                    tweet.user.follow()
                    
                api.update_status(status="YOU'RE breathtaking!",
                                  in_reply_to_status_id=tweet.id)
                
    return new_since_id

def main():
    
    api = create_api()
    since_id = 1
    print(since_id)
    since_id = check_mentions(api, ["help", "support"], since_id)

if __name__ == "MAIN":
    main()