from tweepy import OAuthHandler, API
import logging


class SocialMediaManager():
    def __init__(self, config):
        self.socialmedia_config = config

    def share_on_twitter(self, tweet):
        """
        share a link on twitter
        :param tweet:
        :return:
        """
        consumer_key = self.socialmedia_config.get("Twitter").get("consumer_key")
        consumer_secret = self.socialmedia_config.get("Twitter").get("consumer_secret")
        access_token = self.socialmedia_config.get("Twitter").get("access_token")
        access_token_secret = self.socialmedia_config.get("Twitter").get("access_token_secret")

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = API(auth)
        api.update_status(tweet)
        logging.info("%s has been tweeted" % tweet)
