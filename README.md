# Wren

![ScreenShot](/docs/images/wren.jpg)

Wren is a tool that enables users to monitor, discover and explore daily news stories.

As some readers (including myself) want to read the news beyond their cozy filter bubble, Wren has been designed as an experiment to explore, read and listen to news stories through conversational interfaces (Slack,.. etc). 


## What is Wren ? 

Wren is a system that allows users to automatically parse news content from myriad sources, use NLP technology to enrich news discovery, and store data to easily source and search the enriched news data through conversational interfaces. The system consists of three layers: 

(1) **Data Ingestion:** News aggregation layer to monitor, and ingest data from a list of international news sources. The tool can monitor RSS feeds, parse, acquire, and store the content of several online news sources. 

(2) **Data Discovery:** A Content Analysis layer to process and analyze news articles. This modular layer can extract entities, concepts, keywords, taxonomies, perform sentiment analysis on news content and monitor the news popularity on social media. 

(3) **Dialog:** A conversational system, trained using [RASA](https://github.com/RasaHQ/rasa_nlu) to query the enriched news content.

The tool can be also helpful for data journalists to find stories, easily.

The general view of the system is depicted in Figure 1.

![ScreenShot](/docs/images/wren_news_analytics.png)
**Figure 1.** Wren Technical Architecture 

The process starts by listening to RSS Feeds to collect recent published content both raw text and metadata (e.g. date, time, title, news source …), the sources are formatted in [Yaml file](wren/config/rss_feeds.yml). There are three main media types: Article, Podcast, and Video. Once the data is collected, content is processed and analyzed through the discovery services based on the media type (text, audio, video). We use [Kafka, as it’s a scalable, fault-tolerant, publish-subscribe messaging system](https://www.confluent.io/blog/publishing-apache-kafka-new-york-times/) at this stage to ease data processing & ingestion. Data can be stored then to a database, we use MongoDB, a document-based db. Finally, to facilitate the consumption of our services, and make it possible to integrate them in a comprehensive way with other platforms, the enriched news media data are exposed for consumption using conversational layer, powered by RASA. 

In order to build a conversational system, we designed all the intents that users can use to query the data. A survey has been designed to explore how smart assistants are used to consume news. Then, a list of intents has been determined to reflect how people's choices. The full list of intents can be accessed through this [page](/docs/news_assistant.md). We used [Fountain](https://github.com/tzano/fountain), a natural language data augmentation tool, to generate more than [20,000 samples](/wren/data/wren_training_dataset.json). In case you want to build upon the project, you can use the same template to expand it and create more intents that meets your requirements. The file is accessible [here](/wren/data/wren_training_gen_fountain.yaml). 

The idea is to cover the main and the most reliable news sources around the world. We started with dozen of sources, and we are expanding the list to cover more sources. This list of sources does not claim to be a representive sample of all news sources. Recently, Facebook released a list of 1,000 [RSS feeds](https://fbnewsroomus.files.wordpress.com/2016/05/rss-urls.pdf) that it says it uses to crawl for interesting news stories. The goal is to use a similar list to enrich our list of news organizations.


### Functionalities 
- Collecting News Media Content (Articles, Podcasts, Videos) from [different news organizations](wren/config/rss_feeds.yml)
- Extracting entities, concepts, keywords & taxonomies from News Media Content.
- Storing Data in one centralized DB
- We crowdsourced, and trained [the model](/docs/news_assistant.md) with more than 20,000 queries. This [data](/wren/data/wren_training_dataset.json) is freely available for other developers to use. 
- Built Slackbot to query News Media Content through a conversational interface, served by the model.
- Added support to read articles, by converting Article Content (Text) to Audio. 
- Find & Listen to podcasts.
- Find & Watch videos.  


### Project Structure 
- **core** includes main classes to `Article`, `Podcast`, `Video`, `Media Organization`
- **data_ingestion** contains classes to collect data from [different news organizations](wren/config/rss_feeds.yml).
- **data_discovery** contains classes to enrich the data using NLP services.
- **conversations** contains implementations to connect to external messaging platforms 
- **nlu** contains NLU parser to translate questions to queries using wren model
- **actions** contains classes that handles queries like querying news db, sharing content, reading news, listening to podcasts,..etc
- **data** includes training dataset and [Fountain](http://github.com/tzano/Fountain) template if you need to generate and enrich training dataset
- **models** includes models that has been trained using RASA.
- **config** includes all the configuration files. 
- **connectors** contains interfaces and implementation to connect to database engines.

- **docker** includes `docker-compose` along with other `Dockerfiles` to run our services on Docker.



### Getting Started

You can find all the commands to run `Wren` in `Makefile`. There is a `docker-compose` file to launch all the services

- Build
```bash
$ build
```

alternatively, you can navigate to `docker folder`, build the images `docker-compose build` and launch the services `docker-compose up -d` 

- Check the existing containers 
```bash
$ docker-compose ps
```

- Connect to the container
```bash
$ docker exec -it wren_app sh
```

- Inspect servers in the network
```bash
$ docker inspect docker_wren_network
```

- Train your NLU model, you will find it under `./model/` folder
```bash
python -m rasa_nlu.train -c config/nlu_config.json
```

- Test Rasa Server
```bash
curl 'http://<SERVER>:<PORT>/status'
```


### Configuration Files 
In order to better manage the project, we use 4 main configuration files

- MongoDB configuration file `db.yml`
- RSS Feeds configuration file `rss_feeds.yml`
- Supported discovery services configuration file `services.yml`
- Social Services keys file `keys.yml`
- Messaging Platforms `messaging_platforms.yml`


### Services 

Some of third-party services use libraries that can be downloaded, and installed locally. We use `resources` folder to store these materials.

* SentStrength: 
You need to download `SentStrength.jar` and `SentStrength_data` dictionaries from SentStrength website. 
 
* Standford NER: 
You need to download a 151M zipped file (mainly consisting of classifier data objects) from [Stanford Named Entity Recognizer (NER) website](https://nlp.stanford.edu/software/CRF-NER.shtml)


## Tests

```sh
python -m wren.tests.test_news_scrapers
python -m wren.tests.test_content_parser
python -m wren.tests.test_content_summarizer
python -m wren.tests.test_sentiment_analyzer
python -m wren.tests.test_social_popularity
python -m wren.tests.test_transcriber
```

## Demo

![ScreenShot](/docs/images/wren_slack.png)
**Figure 2.** Wren Slack Chatbot

## References
- [Why messaging is the future of the news brand](https://splinternews.com/why-messaging-is-the-future-of-the-news-brand-1793854684) by Felix Salmon

## Support
If you are having issues, please let us know or submit a pull request.

## Acknowledgement
The project uses RSS feeds and APIs to get news content. The content is not distributed, used only for non-profit research project. 

## License
The project is licensed under the MIT License.
