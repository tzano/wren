# -*- coding: utf-8 -*-
from resources.constants import HOST, PORT, KAFKA, MONGODB, ARTICLES, PODCASTS, VIDEOS, COLLECTION_ARTICLES, \
    COLLECTION_PODCASTS, COLLECTION_VIDEOS
from dateutil import parser

class NewsQuester():
    """
        Find / Fiter Content
    """

    def __init__(self, db_connector, db_config):
        """
        :param db_connector: mongodb cursor
        :type db_connector: cursor

        :param db_config: mongodb configuration file
        :type db_config: dict

        """
        self.db_config = db_config
        self.db_connector = db_connector

    def get_content(self, articles=True, podcasts=True, videos=True):
        """
        get all content (articles, podcasts, videos)

        :param articles: True if we need to get articles
        :type articles: Boolean

        :param podcasts: True if we need to get podcasts
        :type podcasts: Boolean

        :param videos: True if we need to get videos
        :type videos: Boolean

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        try:
            response = {"status": "ok"}
            if articles:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({}, {'_id': 0}))
            if podcasts:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({}, {'_id': 0}))
            if videos:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def find_content(self, keyword, articles=True, podcasts=True, videos=True):
        """
        find content (articles, podcasts, videos) based on a keyword

        :param keyword: keyword to filter data
        :type keyword: String

        :param articles: True if we need to get articles
        :type articles: Boolean

        :param podcasts: True if we need to get podcasts
        :type podcasts: Boolean

        :param videos: True if we need to get videos
        :type videos: Boolean

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        try:
            response = {"status": "ok"}
            if articles:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({'$text': {"$search": keyword}}, {'_id': 0}))
            if podcasts:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({'$text': {"$search": keyword}}, {'_id': 0}))
            if videos:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({'$text': {"$search": keyword}}, {'_id': 0}))
            return response
        except Exception as e:
            return {"status": "bad"}


    def filter_content_by_location(self, keyword, articles=True, podcasts=True, videos=True):
        """
        find content (articles, podcasts, videos) based on a keyword

        :param keyword: keyword to filter data
        :type keyword: String

        :param articles: True if we need to get articles
        :type articles: Boolean

        :param podcasts: True if we need to get podcasts
        :type podcasts: Boolean

        :param videos: True if we need to get videos
        :type videos: Boolean

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        try:
            response = {"status": "ok"}
            if articles:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"entities": {"location": keyword}}, {'_id': 0}))
            if podcasts:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"entities": {"location": keyword}}, {'_id': 0}))
            if videos:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"entities": {"location": keyword}}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}


    def filter_content_by_time(self, from_date, to_date, articles=True, podcasts=True, videos=True):
        """
        Filter tweets from datetime datefrom to dateto

        :param from_date: starting date
        :type from_date: Str

        :param to_date: end date
        :type to_date: Str

        :param articles: True if we need to get articles
        :type articles: Boolean

        :param podcasts: True if we need to get podcasts
        :type podcasts: Boolean

        :param videos: True if we need to get videos
        :type videos: Boolean

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        from_date = parser.parse(from_date)
        to_date = parser.parse(to_date)

        try:
            response = {"status": "ok"}
            if articles:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"pub_date":{'$gte':from_date,'$lt':to_date}}, {'_id': 0}))
            if podcasts:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"pub_date":{'$gte':from_date,'$lt':to_date}}, {'_id': 0}))
            if videos:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"pub_date":{'$gte':from_date,'$lt':to_date}}, {'_id': 0}))

            return response
        except:
            return {"status": "bad"}

    def filter_content_by_location(self, keyword, articles=True, podcasts=True, videos=True):
        """
        find content (articles, podcasts, videos) based on a keyword

        :param keyword: keyword to filter data
        :type keyword: String

        :param articles: True if we need to get articles
        :type articles: Boolean

        :param podcasts: True if we need to get podcasts
        :type podcasts: Boolean

        :param videos: True if we need to get videos
        :type videos: Boolean

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        try:
            response = {"status": "ok"}
            if articles:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"news_media_org": keyword}, {'_id': 0}))
            if podcasts:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"news_media_org": keyword}, {'_id': 0}))
            if videos:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"news_media_org": keyword}, {'_id': 0}))

            return response
        except:
            return {"status": "bad"}

    def filter_content_by_language(self, keyword, articles=True, podcasts=True, videos=True):
        """
        find content (articles, podcasts, videos) based on a keyword

        :param keyword: keyword to filter data
        :type keyword: String

        :param articles: True if we need to get articles
        :type articles: Boolean

        :param podcasts: True if we need to get podcasts
        :type podcasts: Boolean

        :param videos: True if we need to get videos
        :type videos: Boolean

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        try:
            response = {"status": "ok"}
            if articles:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"language": keyword}, {'_id': 0}))
            if podcasts:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"language": keyword}, {'_id': 0}))
            if videos:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"language": keyword}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

