# -*- coding: utf-8 -*-
from resources.constants import EMPTY_STR, EMPTY_LIST, EMPTY_DICT
from dateutil import parser

class Podcast():
    """
    Podcast class 
    """

    def __init__(self, title, podcast_url, **kwargs):
        """
        Initialize the class with you title and podcast_url, other meta information are passed via kwargs.

        :param title: The Podcast's title 
        :type title: :py:class:`str`

        :param podcast_url: The Podcast's url
        :type podcast_url: :py:class:`str`

        :param pub_date: The Podcast's publication date
        :type pub_date: :datetime:class:`datetime`
    
        :param summary: The Podcast's summary 
        :type summary: :py:class:`str`

        :param podcast_content: The Podcast's content 
        :type podcast_content: :py:class:`str`

        :param podcast_subtitle: The Podcast's subtitle 
        :type podcast_subtitle: :py:class:`str`

        :param podcast_metadata: The Podcast's metadata 
        :type podcast_metadata: :py:class:`dict`

        :param authors: The Podcast's authors 
        :type authors: :py:class:`list`

        :param thumbnail: The Podcast's thumbnail 
        :type thumbnail: :py:class:`str`

        :param images: The Podcast's related images 
        :type images: :py:class:`list`

        :param keywords: The Podcast's related keywords 
        :type keywords: :py:class:`list`

        :param category: The Podcast's category 
        :type category: :py:class:`str`

        :param language: The Podcast's language 
        :type language: :py:class:`str`

        :param media_org: The Podcast's source 
        :type media_org: :py:class:`str`

        :return: 
        """
        self.title = title.encode("utf-8")
        self.podcast_url = podcast_url
        self.pub_date = kwargs.get("pub_date", EMPTY_STR)
        self.summary = kwargs.get("summary", EMPTY_STR).encode("utf-8")
        self.podcast_content = kwargs.get("podcast_content", EMPTY_STR).encode("utf-8")
        self.podcast_subtitle = kwargs.get("podcast_subtitle", EMPTY_STR).encode("utf-8")
        self.podcast_metadata = kwargs.get("podcast_metadata", EMPTY_DICT)
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
        return 'PODCAST\n Title: {}\n Publication Date: {}\n Link: {}\n Source: {}\n'.format(self.title, self.pub_date,
                                                                                             self.podcast_url,
                                                                                             self.media_org)

    def json(self):
        return {"title": self.title,
                "podcast_url": self.podcast_url,
                "pub_date": parser.parse(self.pub_date) if dt_to_str else self.pub_date,
                "summary": self.summary,
                "podcast_content": self.podcast_content,
                "podcast_subtitle": self.podcast_subtitle,
                "podcast_metadata": self.podcast_metadata,
                "authors": self.authors,
                "thumbnail": self.thumbnail,
                "images": self.images,
                "keywords": self.keywords,
                "category": self.category,
                "language": self.language,
                "media_type": "Podcast",
                "news_source": self.media_org,
                "popularity": self.popularity_summary,
                "sentiment": self.sentiment_score,
                "entities": self.text_entities}
