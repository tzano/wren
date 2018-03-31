
from models.scheduler import Scheduler
from threading import Thread
import logging
import time
from resources.constants import WSJ, USTODAY, GUARDIAN, THEGLOBAEANDMAIL, TELEGRAPH, REUTERS, NYTIMES, NYPOST, \
    HUFFINGTONPOST, CNN, ALJAZEERA, BBC, MEDIA_TYPE_PODCASTS, EMPTY_STR, EMPTY_DICT, EMPTY_LIST, EN_LANG
from data_ingestion.media_org import NewsMediaOrg


class PodcastsCrawler(Scheduler):
    """
    Podcasts class
    """

    def get_podcasts(self):
        """
        get podcasts

        :return:
        """
        media_sources = [
            NewsMediaOrg(news_org=WSJ, media_types=MEDIA_TYPE_PODCASTS),
            NewsMediaOrg(news_org=NYTIMES, media_types=MEDIA_TYPE_PODCASTS)
        ]

        for podcasts_ingestor in media_sources:
            logging.info("Getting Podcasts from {}".format(podcasts_ingestor))
            for podcast in podcasts_ingestor.parse_podcasts():
                yield podcast

    def run(self):
        """
        run the thread

        :return:
        """
        while True:
            try:
                logging.info("Getting Podcasts")
                for podcast in self.get_podcasts():
                    if podcast:
                        self.kafka_producer.send(self.kafka_topic, podcast.json())

                time.sleep(self.seconds)

            except Exception as e:
                raise e
