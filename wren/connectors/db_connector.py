import pymongo
from pymongo import MongoClient
import logging


class DBConnector:
    """
    Class to connect to mongodb using pymongo
    """

    def __init__(self, config_file):
        """
        Initialize database using config_file

        :param config_file: configuration file that holds information on host, port and db_name
        :type config_file: :py:class:`dict`

        """
        self.config = config_file
        self.host = self.config["host"]
        self.port = self.config["port"]
        self.db_name = self.config["db_name"]
        self.connection = MongoClient(self.host, self.port)


    def connect(self):
        """
        Connect to mongodb database
        """
        try:
            self.connection = MongoClient(self.host, self.port, connect=False)
        except pymongo.errors.ConnectionFailure:
            logging.warn("Could not connect to MongoDB" )

        return self.connection


    def connect_to_collection(self, collection_name):
        """
        :param collection_name: the name of collection
        :type collection_name: :py:class:`str`

        """
        try:
            connection = MongoClient(self.host, self.port)
            data = connection[self.config["db_name"]][collection_name]
        except pymongo.errors.ConnectionFailure:
            logging.warn("Could not connect to MongoDB")
            data = None

        return data
