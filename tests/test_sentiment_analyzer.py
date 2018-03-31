# coding=utf-8

import types
import six
import unittest


from wren.data_discovery.sentiment_analyzer.labmt import LabMT
from wren.data_discovery.sentiment_analyzer.sentistrength import SentiStrength
from wren.resources.constants import ARTICLES, PODCASTS, VIDEOS, SCHEDULER_NEWS_ARTICLES, SCHEDULER_PODCASTS, SCHEDULER_VIDEOS, CONFIG_DIR, DB_CONFIG_FILE, PARAM_CONFIG_FILE,APP_KEYS_FILE,  COLLECTION_ARTICLES, COLLECTION_PODCASTS, COLLECTION_VIDEOS, CALAIS_KEY, DBPEDIA_KEY, FREEBASE_KEY, YAHOO_KEY, ZEMANTA_KEY


class SentimentAnalyzerTests(unittest.TestCase):
    def test_labmt(self):
        labmt = LabMT()
        pos_example = labmt.score_emotion('I love watching basketball')
        neg_example = labmt.score_emotion('I hate watching football')
        self.assertNotEqual(None, pos_example )
        self.assertNotEqual(None, neg_example )

    def test_sentistrength(self):
        sentistrength = SentiStrength()
        result = sentistrength.score_sentiment('I love watching basketball')
        self.assertNotEqual(None, result )

if __name__ == '__main__':
    unittest.main()