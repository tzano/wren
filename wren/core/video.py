# -*- coding: utf-8 -*-
from resources.constants import EMPTY_STR, EMPTY_LIST, EMPTY_DICT
from dateutil import parser

class Video():
    """
    Video class 
    """

    def __init__(self, title, video_url, **kwargs):
        """
        Initialize the class with you title and url, other meta information are passed via kwargs.
    

        :param title: The Video's title 
        :type title: :py:class:`str`

        :param video_url: The Video's url
        :type video_url: :py:class:`str`

        :param pub_date: The Video's publication date
        :type pub_date: :datetime:class:`datetime`
    
        :param summary: The Video's summary 
        :type summary: :py:class:`str`

        :param video_content: The Video's content 
        :type video_content: :py:class:`str`

        :param video_subtitle: The Video's subtitle 
        :type video_subtitle: :py:class:`str`

        :param video_metadata: The Video's metadata 
        :type video_metadata: :py:class:`dict`

        :param authors: The Video's authors 
        :type authors: :py:class:`list`

        :param thumbnail: The Video's thumbnail 
        :type thumbnail: :py:class:`str`

        :param images: The Video's related images 
        :type images: :py:class:`list`

        :param keywords: The Video's related keywords 
        :type keywords: :py:class:`list`

        :param category: The Video's category 
        :type category: :py:class:`str`

        :param language: The Video's language 
        :type language: :py:class:`str`

        :param media_org: The Video's source 
        :type media_org: :py:class:`str`

        """

        self.title = title.encode("utf-8")
        self.video_url = video_url
        self.pub_date = kwargs.get("pub_date", EMPTY_STR)
        self.summary = kwargs.get("summary", EMPTY_STR).encode("utf-8")
        self.video_content = kwargs.get("video_content", EMPTY_STR).encode("utf-8")
        self.video_subtitle = kwargs.get("video_subtitle", EMPTY_STR).encode("utf-8")
        self.video_metadata = kwargs.get("video_metadata", EMPTY_DICT)
        self.authors = kwargs.get("author", EMPTY_LIST)
        self.thumbnail = kwargs.get("thumbnail", EMPTY_STR).encode("utf-8")
        self.images = kwargs.get("images", EMPTY_LIST)
        self.keywords = kwargs.get("keywords", EMPTY_LIST)
        self.category = kwargs.get("category", EMPTY_STR)
        self.language = kwargs.get("language", EMPTY_STR)
        self.concepts = {}
        self.media_org = kwargs.get("media_org", EMPTY_STR)

        self.popularity_summary = kwargs.get("popularity", EMPTY_STR)
        self.sentiment_score = kwargs.get("sentiment", EMPTY_STR)
        self.text_entities = kwargs.get("entities", EMPTY_STR)

    def __str__(self):
        return ("VIDEO\n Title: {}\n Publication Date: {}\n Link: {}\n Source: {}\n".format(self.title, self.pub_date,
                                                                                            self.video_url,
                                                                                            self.video_url,
                                                                                            self.media_org))

    def json(self, dt_to_str=False):
        return {"title": self.title,
                "video_url": self.video_url,
                "pub_date": parser.parse(self.pub_date) if dt_to_str else self.pub_date,
                "summary": self.summary,
                "video_content": self.video_content,
                "video_subtitle": self.video_subtitle,
                "video_metadata": self.video_metadata,
                "authors": self.authors,
                "thumbnail": self.thumbnail,
                "images": self.images,
                "keywords": self.keywords,
                "category": self.category,
                "language": self.language,
                "concepts": self.concepts,
                "media_type": "Video",
                "news_source": self.media_org,
                "popularity": self.popularity_summary,
                "sentiment": self.sentiment_score,
                "entities": self.text_entities
                }
