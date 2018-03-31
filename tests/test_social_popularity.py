# coding=utf-8

import types
import six
import unittest

from wren.data_discovery.social_popularity.social_shares import SocialShares
from wren.resources.constants import ARTICLES, PODCASTS, VIDEOS, SCHEDULER_NEWS_ARTICLES, SCHEDULER_PODCASTS, \
    SCHEDULER_VIDEOS, CONFIG_DIR, DB_CONFIG_FILE, PARAM_CONFIG_FILE, APP_KEYS_FILE, COLLECTION_ARTICLES, \
    COLLECTION_PODCASTS, COLLECTION_VIDEOS, CALAIS_KEY, DBPEDIA_KEY, FREEBASE_KEY, YAHOO_KEY, ZEMANTA_KEY


class SocialPopularityTests(unittest.TestCase):

    def test_get_twitter_shares(self):
        social_shares = SocialShares()
        link_to_article = "http://www.nytimes.com"
        nbr_shares = social_shares.get_twitter_shares(url=link_to_article)
        self.assertNotEqual(None, nbr_shares)

    def test_get_fb_shares(self):
        social_shares = SocialShares()
        link_to_article = "http://www.nytimes.com"
        nbr_shares = social_shares.get_fb_shares(url=link_to_article)
        self.assertNotEqual(None, nbr_shares)

    def test_get_reddit_shares(self):
        social_shares = SocialShares()
        link_to_article = "http://www.nytimes.com"
        nbr_shares = social_shares.get_reddit_shares(url=link_to_article)
        self.assertNotEqual(None, nbr_shares)

    def test_get_stumbles(self):
        social_shares = SocialShares()
        link_to_article = "http://www.nytimes.com"
        nbr_shares = social_shares.get_stumbles(url=link_to_article)
        self.assertNotEqual(None, nbr_shares)

    def test_get_pins(self):
        social_shares = SocialShares()
        link_to_article = "http://www.nytimes.com"
        nbr_shares = social_shares.get_pins(url=link_to_article)
        self.assertNotEqual(None, nbr_shares)

    def test_get_linkedin_shares(self):
        social_shares = SocialShares()
        link_to_article = "http://www.nytimes.com"
        nbr_shares = social_shares.get_linkedin_shares(url=link_to_article)
        self.assertNotEqual(None, nbr_shares)


if __name__ == '__main__':
    unittest.main()
