from kafka import KafkaConsumer, KafkaProducer
from threading import Thread
import binascii
import ast
import logging
import pymongo

class DataFetcher(Thread):
    """
    DataFetcher Class to monitor, and store data into MongoDB
    """

    def __init__(self, kafka_server, kafka_topic, mongo_db_collection):
        """
        Fetching data from kafka and insert it to mongodb

        :param kafka_server: uri of kafka's server
        :type kafka_server: :py:class:`str`

        :param kafka_topic: name of kafka topic
        :type kafka_topic: :py:class:`str`

        :param mongo_db_collection: mongodb cursor
        :type mongo_db_collection: cursor

        """
        Thread.__init__(self)
        self.kafka_consumer = KafkaConsumer(bootstrap_servers=[kafka_server], auto_offset_reset='earliest',
                                            value_deserializer=lambda x: binascii.unhexlify(x).decode('utf-8'))
        self.mongo_db_collection = mongo_db_collection
        self.kafka_topic = kafka_topic

    def run(self):
        """
        monitor up-coming data, process it and insert it into MongoDB
        """
        self.kafka_consumer.subscribe(self.kafka_topic)
        for message in self.kafka_consumer:
            try:
                self.mongo_db_collection.insert(ast.literal_eval(message.value))
            except pymongo.errors.DuplicateKeyError:
                pass
            logging.info("Article has been inserted to DB")

    def clean_message(self, message):
        """
        clean message that comes from Kafka Producer

        :param message: message in json format
        :type message: :py:class:`dict`
        """
        del message['_id']

        return message
