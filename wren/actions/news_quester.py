# -*- coding: utf-8 -*-
from resources.constants import HOST, PORT, KAFKA, MONGODB, ARTICLES, PODCASTS, VIDEOS, COLLECTION_ARTICLES, \
    COLLECTION_PODCASTS, COLLECTION_VIDEOS

from dateutil import parser
from datetime import datetime
import re

class NewsQuester():
    """
        Find / Fiter Content
    """

    def __init__(self, db_connector, db_config, **kw):
        """
        :param db_connector: mongodb cursor
        :type db_connector: cursor

        :param db_config: mongodb configuration file
        :type db_config: :py:class:`dict`

        """
        super(NewsQuester,self).__init__(**kw)
        self.db_config = db_config
        self.db_connector = db_connector

    def get_content_type(self, content_type):
        """
        determin content type

        :param content_type:
        :return: (is_article, is_podcast, is_video)
        """
        if content_type in {"article", "articles", "piece"}:
            is_article = True
        elif content_type in {"podcast", "podcasts"}:
            is_podcast = True
        elif content_type in {"video", "tv show", "show", "television program"}:
            is_video = True

        return is_article, is_podcast, is_video

    def get_content(self, content_type):
        """
        get all content (articles, podcasts, videos)

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        is_article, is_podcast, is_video = self.get_content_type(content_type)
        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def find_content(self, keyword, content_type=None):
        """
        find content (articles, podcasts, videos) based on a keyword

        :param keyword: keyword to filter data
        :type keyword: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """
        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({'$text': {"$search": keyword}}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({'$text': {"$search": keyword}}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({'$text': {"$search": keyword}}, {'_id': 0}))
            return response
        except Exception as e:
            return {"status": "bad"}

    def filter_content_by_orgname(self, org_name, content_type=None):
        """
        find content (articles, podcasts, videos) based on a title

        :param org_name: organization name
        :type org_name: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"news_media_org": re.compile(org_name, re.IGNORECASE)}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"news_media_org": re.compile(org_name, re.IGNORECASE)}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"news_media_org": re.compile(org_name, re.IGNORECASE)}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def filter_content_by_title(self, title, content_type=None):
        """
        find content (articles, podcasts, videos) based on a title

        :param title: title
        :type title: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"article_headline": title}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"title": title}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"title": title}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def filter_content_by_authors(self, authors, content_type=None):
        """
        find content (articles, podcasts, videos) via author

        :param authors: title
        :type authors: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"authors": {"$in": authors}}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find( {"authors": {"$in": authors}}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"authors": {"$in": authors}}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def filter_content_by_person(self, person, content_type=None):
        """
        find content (articles, podcasts, videos) via person

        :param person: title
        :type person: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({'$text': {"$search": person}}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({'$text': {"$search": person}}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({'$text': {"$search": person}}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def filter_content_by_location(self, keyword, content_type=None):
        """
        find content (articles, podcasts, videos) based on a location

        :param keyword: keyword to filter data
        :type keyword: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"location": keyword}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find( {"location": keyword}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"location": keyword}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def filter_content_by_time(self, to_date, content_type=None):
        """
        Filter tweets from datetime datefrom to dateto

        :param to_date: end date
        :type to_date: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        from_date = datetime.now()
        to_date = parser.parse(to_date)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(
                    db_articles.find({"pub_date": {'$gte': from_date, '$lt': to_date}}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(
                    db_podcasts.find({"pub_date": {'$gte': from_date, '$lt': to_date}}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"pub_date": {'$gte': from_date, '$lt': to_date}}, {'_id': 0}))

            return response
        except:
            return {"status": "bad"}

    def filter_content_by_language(self, keyword, content_type=None):
        """
        find content (articles, podcasts, videos) based on a keyword

        :param keyword: keyword to filter data
        :type keyword: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"language": keyword}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"language": keyword}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"language": keyword}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def filter_content_by_topic(self, topic, content_type=None):
        """
        find content (articles, podcasts, videos) based on a topic

        :param topic: keyword to filter data
        :type topic: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :return: json object {"status": "ok", "articles": <articles>, "podcasts": <podcasts>, "videos": <videos>})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                response["articles"] = list(db_articles.find({"category": topic}, {'_id': 0}))
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                response["podcasts"] = list(db_podcasts.find({"category": topic}, {'_id': 0}))
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                response["videos"] = list(db_videos.find({"category": topic}, {'_id': 0}))
            return response
        except:
            return {"status": "bad"}

    def update_content_by_title(self, title, content_type=None, **kwargs):
        """
        update content (articles, podcasts, videos) based on a title
        & add a new field

        :param title: title
        :type title: :py:class:`str`

        :param content_type: type of content
        :type content_type: :py:class:`str`

        :param kwargs:
        :type kwargs: :py:class:`dict`

        :return: json object {"status": "ok/bad"})
        """

        if content_type is None:
            is_article, is_podcast, is_video = True, True, True
        else:
            is_article, is_podcast, is_video = self.get_content_type(content_type)

        value = {}
        # name of collection
        if kwargs.get('collection', None) is not None:
            value["collection"] = kwargs['collection']
        # is bookmarked or no
        if kwargs.get('is_bookmarked', None) is not None:
            value["is_bookmarked"] = kwargs['is_bookmarked']

        try:
            response = {"status": "ok"}
            if is_article:
                db_articles = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_ARTICLES])
                db_articles.update_one({"article_headline": title}, {"$set": value})
            if is_podcast:
                db_podcasts = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_PODCASTS])
                db_podcasts.update_one({"title": title}, {"$set": value})
            if is_video:
                db_videos = self.db_connector.connect_to_collection(self.db_config[MONGODB][COLLECTION_VIDEOS])
                db_videos.update_one({"title": title}, {"$set": value})
            return response
        except:
            return {"status": "bad"}
