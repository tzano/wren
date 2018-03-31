# -*- coding: utf-8 -*-
import yaml
from data_ingestion.news_articles_crawler import NewsArticlesCrawler
from data_ingestion.podcasts_crawler import PodcastsCrawler
from data_ingestion.videos_crawler import VideosCrawler
from connectors.db_connector import DBConnector
from resources.constants import HOST, PORT, KAFKA, MONGODB, ARTICLES, PODCASTS, VIDEOS, SCHEDULER_NEWS_ARTICLES, \
    SCHEDULER_PODCASTS, SCHEDULER_VIDEOS, CONFIG_DIR, DB_CONFIG_FILE, PARAM_CONFIG_FILE, COLLECTION_ARTICLES, \
    COLLECTION_PODCASTS, COLLECTION_VIDEOS
from data_ingestion.data_consumer import DataFetcher
import logging
from resources.utils import load_yaml

logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    # ---------------------- #
    # Configuration Files
    # ---------------------- #
    db_config = load_yaml(CONFIG_DIR, DB_CONFIG_FILE)
    param_config = load_yaml(CONFIG_DIR, PARAM_CONFIG_FILE)
    # Connect to Kafka/MongoDB
    kafka_server = "{}:{}".format(db_config[KAFKA][HOST], db_config[KAFKA][PORT])
    db_connector = DBConnector(db_config[MONGODB])

    # # ---------------------- #
    # # Data Ingestion
    # # ---------------------- #
    # # News Articles Crawler
    if param_config[ARTICLES]:
        db_articles = db_connector.connect_to_collection(db_config[MONGODB][COLLECTION_ARTICLES])
        news_articles_crawler = NewsArticlesCrawler(name=SCHEDULER_NEWS_ARTICLES,
                                                    kafka_server=kafka_server,
                                                    kafka_topic=db_config[KAFKA][ARTICLES])
        news_articles_crawler.start()
        news_articles_fetcher = DataFetcher(kafka_server, db_config[KAFKA][ARTICLES], db_articles)
        news_articles_fetcher.start()

    # Podcast Crawler
    if param_config[PODCASTS]:
        db_podcasts = db_connector.connect_to_collection(db_config[MONGODB][COLLECTION_PODCASTS])
        podcasts_crawler = PodcastsCrawler(name=SCHEDULER_PODCASTS,
                                           kafka_server=kafka_server,
                                           kafka_topic=db_config[KAFKA][PODCASTS])
        podcasts_crawler.start()
        podcasts_fetcher = DataFetcher(kafka_server, db_config[KAFKA][PODCASTS], db_podcasts)
        podcasts_fetcher.start()

    # Video Crawler
    if param_config[VIDEOS]:
        db_videos = db_connector.connect_to_collection(db_config[MONGODB][COLLECTION_VIDEOS])
        news_videos_crawler = VideosCrawler(name=SCHEDULER_VIDEOS,
                                            kafka_server=kafka_server,
                                            kafka_topic=db_config[KAFKA][VIDEOS])
        news_videos_crawler.start()
        news_videos_fetcher = DataFetcher(kafka_server, db_config[KAFKA][VIDEOS], db_videos)
        news_videos_fetcher.start()
