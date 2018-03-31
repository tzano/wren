from models.scheduler import Scheduler
import logging
import time
from resources.constants import WSJ, VICE, USTODAY, GUARDIAN, THEGLOBAEANDMAIL, TELEGRAPH, REUTERS, NYTIMES, NYPOST, \
    CNN, ALJAZEERA, BBC, MEDIA_TYPE_ARTICLES, EMPTY_STR, EMPTY_DICT, EMPTY_LIST, EN_LANG
from data_ingestion.media_org import NewsMediaOrg
import json
import binascii

class NewsArticlesCrawler(Scheduler):
    """
    News Articles class
    """

    def get_news_articles(self):
        """
        get news articles.

        :return: generator
        """
        news_sources = [
            NewsMediaOrg(news_org=ALJAZEERA, media_types=MEDIA_TYPE_ARTICLES)
            # NewsMediaOrg(news_org=BBC, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=CNN, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=NYPOST, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=NYTIMES, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=REUTERS, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=TELEGRAPH, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=THEGLOBAEANDMAIL, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=GUARDIAN, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=USTODAY, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=VICE, media_types=MEDIA_TYPE_ARTICLES),
            # NewsMediaOrg(news_org=WSJ, media_types=MEDIA_TYPE_ARTICLES)
        ]
        for news_ingestor in news_sources:
            logging.info("Getting articles from {}".format(news_ingestor))
            for article in news_ingestor.parse_articles():
                yield article

    def run(self):
        """
        run the thread

        """

        while True:
            try:
                for article in self.get_news_articles():
                    if article:
                        self.kafka_producer.send(self.kafka_topic, str(article.json()))
                time.sleep(self.seconds)

            except Exception as e:
                raise e
