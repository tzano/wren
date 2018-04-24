from abc import ABCMeta, abstractmethod
from time import sleep
import logging
from resources.constants import STOPPED, RUNNING, SECONDS
from kafka import KafkaProducer
from threading import Thread
import json
import binascii

class Scheduler(Thread):
    __metaclass__ = ABCMeta

    """
    Scheduler Abstract Class 
    """

    def __init__(self, name, kafka_server, kafka_topic, *args, **kwargs):
        """
        Initialize the class with you title and podcast_url, other meta information are passed via kwargs.

        :param name: The Scheduler's name
        :type name: :py:class:`str`

        :param db_collection: The collection's name
        :type db_collection: :pymongo:class:` `
        
        :param kafka_topic: name of kafka topic
        :type kafka_topic: :py:class:`str`

        :param args: args
        :type args: :py:class:`dict`

        :param kwargs: kwargs 
        :type kwargs: :py:class:`dict`

        """
        super(Scheduler, self).__init__()
        self.name = name
        self.kafka_producer = KafkaProducer(bootstrap_servers=[kafka_server], value_serializer=lambda v: binascii.hexlify(v.encode('utf-8')))
        self.kafka_topic = kafka_topic
        self.seconds = SECONDS
        self._stopped = False

    def _decorate_task(self):
        """
        decorate task
        """

        def result():
            while (not self._stopped):
                try:
                    self.code()
                except Exception as e:
                    logging.warn('Exception: %s occured. ' % e)

                sleep(self.seconds)

        return result

    def status(self):
        """
        get status
        """
        if self._stopped:
            return STOPPED
        return RUNNING

    def stop(self):
        """
        stop the scheduler
        """
        self._stopped = True

    def resume(self):
        """
        resume the scheduler
        """
        self._stopped = False
        self.run()

    def get_news_articles(self):
        """
        get news articles
        """
        raise NotImplementedError

    def get_podcasts(self):
        """
        get podcasts 
        """
        raise NotImplementedError

    def get_videos(self):
        """
        get videos
        """
        raise NotImplementedError

    @abstractmethod
    def run(self):
        pass

    def __unicode__(self):
        return self.name
