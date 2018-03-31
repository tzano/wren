# coding=utf-8

import unittest

from os.path import join, dirname, abspath
import yaml
from wren.news_quest.news_quester import NewsQuester
from wren.resources.utils import load_yaml
from wren.connectors.db_connector import DBConnector

from wren.resources.constants import CONFIG_DIR, DB_CONFIG_FILE, MONGODB, COLLECTION_ARTICLES


class NewsQuestTests(unittest.TestCase):
    def setUp(self):
        db_config = load_yaml(CONFIG_DIR, DB_CONFIG_FILE)
        db_connector = DBConnector(db_config[MONGODB])
        self.news_quester = NewsQuester(db_connector, db_config)

    def test_get_content(self):
        data = self.news_quester.get_content()
        self.assertEqual(data.get('status', 'bad'), 'ok')

    def test_find_content(self):
        data = self.news_quester.find_content('Gaza')
        self.assertEqual(data.get('status', 'bad'), 'ok')

    def test_filter_content_by_time(self):
        data = self.news_quester.filter_content_by_time('Fri, 20 Mar 2018 00:00:00 GMT', 'Fri, 31 Mar 2018 18:54:05 GMT')
        self.assertEqual(data.get('status', 'bad'), 'ok')



if __name__ == '__main__':
    unittest.main()
