# -*- coding: utf-8 -*-

from models.article import Article
from models.podcast import Podcast
from models.video import Video
from abc import ABCMeta
from os.path import join, dirname, abspath
import yaml
import feedparser
import logging
import requests
from resources.constants import EMPTY_STR, EMPTY_LIST, EMPTY_DICT, EN_LANG, APP_KEYS_FILE, CALAIS_KEY, CONFIG_FNAME, \
    PAR_DIR, CONFIG_DIR, ARTICLES, PODCASTS, VIDEOS, ARTICLE, \
    PODCAST, VIDEO


class NewsMediaOrg():
    """
    News Media class
    """
    __metaclass__ = ABCMeta

    def __init__(self, news_org, media_types):
        """
        Initialize the class with news_org and media_types.

        :param news_org: name of the organization
        :type news_org: :py:class:`str`

        :param media_types: supported media types by the News Media Organization
        :type media_types: :py:class:`dict`

        """
        self.news_media_org = news_org
        self.media_types = {ARTICLES: media_types.get(ARTICLE, None),
                            PODCASTS: media_types.get(PODCAST, None),
                            VIDEOS: media_types.get(VIDEO, None)}
        self.app_keys = yaml.load(open("{}/{}".format(CONFIG_DIR, APP_KEYS_FILE)))

    def __repr__(self):
        """ repr """
        return self.news_media_org

    def __str__(self):
        """ str """
        return self.news_media_org

    def get_rss_feed(self, media_type, category='All'):
        """
        get news feed url

        :param media_type: type of
        :type media_type: :py:class:`str`

        :param category: category of news rss feed
        :type category: :py:class:`str`

        :return: url of news feed
        """

        fname_path = "{}/{}".format(CONFIG_DIR, CONFIG_FNAME)
        config_json = yaml.load(open(fname_path))

        # _media_type = self.media_types[media_type]

        try:
            url = config_json[media_type][self.news_media_org][category]
        except Exception as e:
            logging.warn('Invalid name for category')
            url = None

        return url

    def parse_rss_feed(self, url):
        """
        generate rss entries of the latest articles from rss feed url.

        :param url: url of news feed
        :type  url: :py:class:`str`

        :return: generator of latest articles
        """
        feed = feedparser.parse(url)
        for entry in feed['entries']:
            yield ({'title': entry.title, 'url': entry.link, 'pub_date': entry.get('published', ''),
                    "summary": entry.get("summary", "")})

    def get_news_media_source(self):
        """
        get the media source (news organization)

        :return: name news media organization
        """
        return self.news_media_org

    # ---------------------------------------- #
    # Methods for data discovery
    # ---------------------------------------- #

    def score_sentiment(self, newsmedia_text):
        """
        score sentiment of the summary of the text

        :param newsmedia_text: text appeared in rss feed
        :type  newsmedia_text: :py:class:`str`

        :return: sentiment score
        """
        sentistrength = SentiStrength()
        sentiment_score = sentistrength.score_sentiment(newsmedia_text)
        return sentiment_score

    def extract_entities(self, newsmedia_text, use_calais= True, use_dbpedia=False):
        """
        extract entities from the text

        :param newsmedia_text: text appeared in rss feed
        :type  newsmedia_text: :py:class:`str`

        :return: dict that contains entities
        """
        calais_result, dbpedia_result = [], []
        if use_calais:
            calais = CalaisAPI(api_key=self.app_keys[CALAIS_KEY])
            calais_result = calais.extract_entities(text=newsmedia_text)
        if use_dbpedia:
            dbpedia_api = DbpediaAPI(api_key=self.app_keys[CALAIS_KEY])
            dbpedia_result = dbpedia_api.extract_entities(text=newsmedia_text)

        return {'Calais': calais_result, 'Dbpedia': dbpedia_result}

    def score_popularity(self, newsmedia_url):
        """
        score popularity on social media

        :param newsmedia_url: url of the article
        :type  newsmedia_url: :py:class:`str`

        :return: dict that contains entities
        """
        social_shares = SocialShares()
        return social_shares.get_social_media_shares(newsmedia_url)

    # ---------------------------------------- #
    # Methods to get Article information
    # ---------------------------------------- #

    def get_article_url(self, entry):
        """
        get the article's url

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('url', EMPTY_STR)

    def get_article_headline(self, entry):
        """
        get the article's headline

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('title', EMPTY_STR)

    def get_article_pub_date(self, entry):
        """
        get the article's publication date

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('pub_date', EMPTY_STR)

    def get_article_summary(self, entry):
        """
        get the article's summary

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('summary', EMPTY_STR)

    def get_article_content(self, entry):
        """
        get the article's content

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_article_html(self, entry):
        """
        get the article's html

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_article_metadata(self, entry):
        """
        get the article's metadata

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_DICT

    def get_article_authors(self, entry):
        """
        get the authors who published article

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_article_thumbnail(self, entry):
        """
        get the article's thumbnail

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_article_images(self, entry):
        """
        get the article's set of images

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_article_videos(self, entry):
        """
        get the article's set of videos

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_article_keywords(self, entry):
        """
        get the article's keywords

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_article_category(self, entry):
        """
        get the article's category

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return EMPTY_STR

    def get_article_language(self, entry):
        """

        :param entry: dict that holds main article information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return EN_LANG

    def parse_article(self, entry):
        """

        parse the article metadata

        :param entry: dict that holds main article information (url, title,.. etc)
        :type entry: :py:class:`dict`

        :return:
        """

        try:
            article_url = self.get_article_url(entry)
            response = requests.get(article_url)
            if response.status_code == 200:
                # soup = BeautifulSoup(response.text, "html.parser")
                article_headline = self.get_article_headline(entry)
                article_pub_dt = self.get_article_pub_date(entry)
                article_summary = self.get_article_summary(entry)
                article_content = self.get_article_content(entry)
                article_html = self.get_article_html(entry)
                article_metadata = self.get_article_metadata(entry)
                article_authors = self.get_article_authors(entry)
                article_images = self.get_article_images(entry)
                article_videos = self.get_article_videos(entry)
                article_keywords = self.get_article_keywords(entry)
                article_category = self.get_article_category(entry)
                article_language = self.get_article_language(entry)
                article_thumbnail = self.get_article_thumbnail(entry)
                article_source = self.get_news_media_source()


                return Article(article_headline=article_headline, article_url=article_url,
                               pub_date=article_pub_dt, summary=article_summary, article_content=article_content,
                               article_html=article_html, article_metadata=article_metadata, authors=article_authors,
                               thumbnail=article_thumbnail, images=article_images, videos=article_videos,
                               keywords=article_keywords,
                               category=article_category, language=article_language, news_media_org=article_source)

            else:
                logging.error("Cannot fetch the article's url!")
                return None

        except Exception as e:
            logging.error("Cannot parse article. Download operation may have failed!")
            return None


    def parse_articles(self, category='All'):
        """
        parse the latest articles

        :return: a generator of latest parsed articles.
        """
        rss_feed = self.get_rss_feed(ARTICLES, category)
        for article_entry in self.parse_rss_feed(rss_feed):
            yield self.parse_article(article_entry)

    # ---------------------------------------- #
    # Methods to get Podcast information
    # ---------------------------------------- #

    def get_podcast_title(self, entry):
        """
        get the podcast's title

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('title', EMPTY_STR)

    def get_podcast_url(self, entry):
        """
        get the podcast's url

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('url', EMPTY_STR)

    def get_podcast_pub_date(self, entry):
        """
        get the podcast's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """

        return entry.get('pub_date', EMPTY_STR)

    def get_podcast_summary(self, entry):
        """
        get the podcast's


        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('summary', EMPTY_STR)

    def get_podcast_content(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('summary', EMPTY_STR)

    def get_podcast_subtitle(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_podcast_metadata(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_DICT

    def get_podcast_authors(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_podcast_thumbnail(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_podcast_images(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_podcast_keywords(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_podcast_category(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_podcast_language(self, entry):
        """
        get the podcast's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return EN_LANG

    def parse_podcast(self, entry):
        """


        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type entry: :py:class:`dict`

        :return:
        """

        try:
            podcast_url = self.get_podcast_url(entry)
            response = requests.get(podcast_url)
            if response.status_code == 200:
                # You can use BeautifulSoup after reading the Website's Terms of Use
                # soup = BeautifulSoup(response.text, "html.parser")
                podcast_title = self.get_podcast_title(entry)
                podcast_pub_dt = self.get_podcast_pub_date(entry)
                podcast_summary = self.get_podcast_summary(entry)
                podcast_content = self.get_podcast_content(entry)
                podcast_metadata = self.get_podcast_metadata(entry)
                podcast_authors = self.get_podcast_authors(entry)
                podcast_images = self.get_podcast_images(entry)
                podcast_keywords = self.get_podcast_keywords(entry)
                podcast_category = self.get_podcast_category(entry)
                podcast_language = self.get_podcast_language(entry)
                podcast_thumbnail = self.get_podcast_thumbnail(entry)
                podcast_source = self.get_news_media_source()


                return Podcast(title=podcast_title, podcast_url=podcast_url,
                               pub_date=podcast_pub_dt, summary=podcast_summary, podcast_content=podcast_content,
                               podcast_metadata=podcast_metadata, authors=podcast_authors,
                               thumbnail=podcast_thumbnail, images=podcast_images,
                               keywords=podcast_keywords,
                               category=podcast_category, language=podcast_language, news_media_org=podcast_source)

            else:
                logging.error("Cannot fetch the article's url!")
                return None

        except Exception as e:
            logging.error("Cannot parse article. Download operation may have failed!")
            return None

    def parse_podcasts(self, category='All'):
        """
        parse the latest articles

        :return: a generator of latest parsed articles.
        """
        rss_feed = self.get_rss_feed(ARTICLES, category)
        for podcast_entry in self.parse_rss_feed(rss_feed):
            yield self.parse_podcast(podcast_entry)

    # ---------------------------------------- #
    # Methods to get Video information
    # ---------------------------------------- #

    def get_video_title(self, entry):
        """
        get the video's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('title', EMPTY_STR)

    def get_video_url(self, entry):
        """
        get the video's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('url', EMPTY_STR)

    def get_video_pub_date(self, entry):
        """
        get the video's



        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('pub_date', EMPTY_STR)

    def get_video_summary(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return entry.get('summary', EMPTY_STR)

    def get_video_content(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_video_subtitle(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_video_metadata(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_DICT

    def get_video_authors(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_video_thumbnail(self, entry):
        """
        get the video's


        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_video_images(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_video_keywords(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_LIST

    def get_video_category(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        logging.warn("This functionality is not implemented yet. You should check the Website's Terms of Use")
        return EMPTY_STR

    def get_video_language(self, entry):
        """
        get the video's

        :param entry: dict that holds main podcast information (url, title,.. etc)
        :type  entry: :py:class:`dict`

        :return:
        """
        return EN_LANG

    def parse_video(self, entry):
        """

        :param entry: dict that holds main video information (url, title,.. etc)
        :type entry: :py:class:`dict`

        :return:
        """

        try:
            video_url = self.get_video_url(entry)
            response = requests.get(video_url)
            if response.status_code == 200:
                # You can use BeautifulSoup after reading the Website's Terms of Use
                # soup = BeautifulSoup(response.text, "html.parser")
                video_headline = self.get_video_title(entry)
                video_pub_dt = self.get_video_pub_date(entry)
                video_summary = self.get_video_summary(entry)
                video_content = self.get_video_content(entry)
                video_metadata = self.get_video_metadata(entry)
                video_authors = self.get_video_authors(entry)
                video_images = self.get_video_images(entry)
                video_keywords = self.get_video_keywords(entry)
                video_category = self.get_video_category(entry)
                video_language = self.get_video_language(entry)
                video_thumbnail = self.get_video_thumbnail(entry)
                video_source = self.get_news_media_source()

                return Video(video_headline=video_headline, video_url=video_url,
                             pub_date=video_pub_dt, summary=video_summary, video_content=video_content,
                             video_metadata=video_metadata, authors=video_authors,
                             thumbnail=video_thumbnail, images=video_images,
                             keywords=video_keywords,
                             category=video_category, language=video_language, news_media_org=video_source)

            else:
                logging.error("Cannot fetch the article's url!")
                return None

        except Exception as e:
            logging.error("Cannot parse article. Download operation may have failed!")
            return None

    def parse_videos(self, category='All'):
        """
        parse the latest videos

        :return: a generator of latest parsed videos.
        """
        rss_feed = self.get_rss_feed(VIDEOS, category)
        for video_entry in self.parse_rss_feed(rss_feed):
            yield self.parse_video(video_entry)
