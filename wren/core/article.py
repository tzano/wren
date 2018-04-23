# -*- coding: utf-8 -*-
from resources.constants import EMPTY_STR, EMPTY_LIST, EMPTY_DICT
import json
from dateutil import parser

class Article():
    """
    Article class 
    """

    def __init__(self, article_headline, article_url, **kwargs):
        """
        Initialize the class with article's headline and url, other meta information are passed via kwargs
        
        :param article_headline: Podcast's title 
        :type article_headline: :py:class:`str`

        :param article_url: The Article's url
        :type article_url: :py:class:`str`

        :param pub_date: The Article's publication date
        :type pub_date: :datetime:class:`datetime`
    
        :param summary: The Article's summary 
        :type summary: :py:class:`str`

        :param article_content: The Article's content 
        :type article_content: :py:class:`str`

        :param article_html: The Article's page html
        :type article_html: :py:class:`str`

        :param article_metadata: The Article's metadata 
        :type article_metadata: :py:class:`dict`

        :param authors: The Article's authors 
        :type authors: :py:class:`list`

        :param thumbnail: The Article's thumbnail 
        :type thumbnail: :py:class:`str`

        :param images: The Article's related images 
        :type images: :py:class:`list`

        :param videos: The Article's related videos 
        :type videos: :py:class:`list`

        :param keywords: The Article's related keywords 
        :type keywords: :py:class:`list`

        :param category: The Article's category 
        :type category: :py:class:`str`

        :param language: The Article's language 
        :type language: :py:class:`str`
        
        :param keywords: The Article's related concepts
        :type keywords: :py:class:`dict`

        :param media_org: The Article's source 
        :type media_org: :py:class:`str`


        """
        self.article_headline = article_headline if article_headline is not None else article_headline
        self.article_url = article_url if article_url is not None else article_url
        self.pub_date = kwargs.get("pub_date", EMPTY_STR)
        self.summary = kwargs.get("summary", EMPTY_STR)
        self.article_content = kwargs.get("article_content", EMPTY_STR)
        self.article_html = kwargs.get("article_html", EMPTY_STR)
        self.article_metadata = kwargs.get("article_metadata", EMPTY_DICT)
        self.authors = kwargs.get("authors", EMPTY_LIST)
        self.thumbnail = kwargs.get("thumbnail", EMPTY_STR)
        self.images = kwargs.get("images", EMPTY_LIST)
        self.videos = kwargs.get("videos", EMPTY_LIST)
        self.keywords = kwargs.get("keywords", EMPTY_LIST)
        self.category = kwargs.get("category", EMPTY_STR)
        self.language = kwargs.get("language", EMPTY_STR)
        self.concepts = {}
        self.media_org = kwargs.get('media_org', EMPTY_STR)
        self.popularity_summary = kwargs.get("popularity", EMPTY_STR)
        self.sentiment_score = kwargs.get("sentiment", EMPTY_STR)
        self.entities = kwargs.get("entities", EMPTY_STR)

    def __str__(self):
        return ("ARTICLE\n Headline: {}\n Publication Date: {}\n Link: {}\n ontent: {}\n Source: {}\n".format(
            self.article_headline, self.pub_date, self.article_url, self.article_content, self.media_org))

    def to_message(self):
        return json.dumps(self.json(dt_to_str=False)).encode('utf-8')

    def json(self, dt_to_str=False):
        return {"article_headline": self.article_headline,
                "article_url": self.article_url,
                "pub_date": parser.parse(self.pub_date) if dt_to_str else self.pub_date,
                "summary": self.summary,
                "article_content": self.article_content,
                "article_html": self.article_html,
                "article_metadata": self.article_metadata,
                "authors": self.authors,
                "thumbnail": self.thumbnail,
                "images": self.images,
                "videos": self.videos,
                "keywords": self.keywords,
                "category": self.category,
                "language": self.language,
                "concepts": self.concepts,
                "media_type": "Article",
                "news_media_org": self.media_org,
                "popularity": self.popularity_summary,
                "sentiment": self.sentiment_score,
                "entities": self.entities}
