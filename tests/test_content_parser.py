# coding=utf-8

import types
import six
import unittest

from wren.data_discovery.content_parser.calais import CalaisAPI
from wren.data_discovery.content_parser.dbpedia import DbpediaAPI
from os.path import join, dirname, abspath
import yaml
from resources.constants import *

APP_KEYS = yaml.load(open(abspath(join(dirname(__file__), PAR_DIR, PAR_DIR, CONFIG_DIR, APP_KEYS_FILE))))

class ContentParserTests(unittest.TestCase):
    def test_opencalais(self):
        calais = CalaisAPI(api_key=APP_KEYS[CALAIS_KEY])
        result = calais.extract_entities(text = "Obama is the president")
        self.assertNotEqual(None, result )

    def test_dbpedia_extract_entities(self):
        dbpedia_api = DbpediaAPI(api_key=APP_KEYS[CALAIS_KEY])
        result = dbpedia_api.extract_entities(text = """President Obama called Wednesday on Congress to extend a tax 
        break for students included in last year's economic stimulus package, arguing that the policy provides more 
        generous assistance.""")
        self.assertNotEqual(None, result )

    def test_dbpedia_keyword_search(self):
        dbpedia_api = DbpediaAPI(api_key=APP_KEYS[CALAIS_KEY])
        result = dbpedia_api.dbpedia_keyword_search(keyword = "Barack Obama")
        self.assertNotEqual(None, result )

    def test_dbpedia_prefix_search(self):
        dbpedia_api = DbpediaAPI(api_key=APP_KEYS[CALAIS_KEY])
        result = dbpedia_api.dbpedia_prefix_search(prefix = "Barack")
        self.assertNotEqual(None, result )

if __name__ == '__main__':
    unittest.main()