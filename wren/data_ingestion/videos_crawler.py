from core.scheduler import Scheduler
from threading import Thread
import logging
import time
from resources.constants import WSJ, VICE, USTODAY, GUARDIAN, THEGLOBAEANDMAIL, TELEGRAPH, REUTERS, NYTIMES, NYPOST, \
    HUFFINGTONPOST, CNN, ALJAZEERA, BBC, MEDIA_TYPE_VIDEOS, EMPTY_STR, EMPTY_DICT, EMPTY_LIST, EN_LANG
from core.media_org import NewsMediaOrg


class VideosCrawler(Scheduler):
    """
    Video class 
    """

    def get_news_videos(self):
        """
        get news videos 
        
        :return: 
        """

        media_sources = [
            NewsMediaOrg(news_org=ALJAZEERA, media_types=MEDIA_TYPE_VIDEOS)
        ]
        for videos_ingestor in media_sources:
            for video in videos_ingestor.parse_videos():
                yield video

    def run(self):
        """
        run the thread
        
        :return: 
        """

        while True:
            try:
                logging.info("Getting Videos")
                for video in self.get_news_videos():
                    if video:
                        self.kafka_producer.send(self.kafka_topic, video.json())

                time.sleep(self.seconds)

            except Exception as e:
                raise e
