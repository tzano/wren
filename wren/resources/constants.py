# config files
CONFIG_DIR = "config"

# Link to DB Configuration
DB_CONFIG_FILE = "db.yml"

# Name of collection
COLLECTION_NAME = 'collection_name'
CONFIG_DIR = "config"
CONFIG_FNAME = "rss_feeds.yml"
PARAM_CONFIG_FILE = "services.yml"
APP_KEYS_FILE = "keys.yml"
NLU_CONFIG = "nlu_config.yml"
MESSAGING_FILE = "messaging_platforms.yml"
SOCIALMEDIA_FILE = "socialmedia.yml"
EMAIL_FILE = "email.yml"
PAR_DIR = ".."


# News Organizations
ALJAZEERA = "AlJazeera"
BBC = "BBC"
CNN = "CNN"
HUFFINGTONPOST = "HuffingtonPost"
NYPOST = "NYPost"
NYTIMES = "NYTimes"
REUTERS = "Reuters"
TELEGRAPH = "Telegraph"
THEGLOBAEANDMAIL = "TheGlobeAndMail"
GUARDIAN = "Guardian"
USTODAY = "USAToday"
VICE = "Vice"
WSJ = "WSJ"

# name of collections
COLLECTION_ARTICLES = 'articles'
COLLECTION_PODCASTS = 'podcasts'
COLLECTION_VIDEOS = 'videos'
COLLECTION_LISTS = 'list'
COLLECTION_BOOKMARS = 'bookmarks'

# Schedulers' names 
SCHEDULER_NEWS_ARTICLES = "Scheduler-NewsArticles"
SCHEDULER_PODCASTS = "Scheduler-Podcasts"
SCHEDULER_VIDEOS = "Scheduler-Videos"

SECONDS = 60

# Empty string 
EMPTY_STR = ""
EMPTY_LIST = []
EMPTY_DICT = {}

# media types
ARTICLES = "Articles"
PODCASTS = "Podcasts"
VIDEOS = "Videos"

ARTICLE = "Article"
PODCAST = "Podcast"
VIDEO = "Video"

MEDIA_TYPE_ARTICLES = {ARTICLES: ARTICLE}
MEDIA_TYPE_PODCASTS = {PODCASTS: PODCAST}
MEDIA_TYPE_VIDEOS = {VIDEOS: VIDEO}

# Scheduler
STOPPED = "stopped"
RUNNING = "running"

# Languages 
EN_LANG = "English"
AR_LANG = "Arabic"

# Keys for webservices
CALAIS_KEY = "calais_key"
DBPEDIA_KEY = "dbpedia_key"
FREEBASE_KEY = "freebase_key"
YAHOO_KEY = "yahoo_key"
ZEMANTA_KEY = "zemanta_key"

VONA_KEY = "vona_key"
VONA_USERNAME = "vona_username"

SLACK_API_KEY = "api_key"
SLACK_BOT_NAME = "bot_name"
SLACK_CHANNEL_NAME = "channel_name"

SLACK_SERVICE = "slack"

# Voice TTs
TTS_PERONA = 'Emma'


# Connectors
MONGODB = "mongodb"
KAFKA = "kafka"

# Host/Port
HOST = "host"
PORT = "port"

SENTISTRENGHT_JAR = "../resources/SentiStrength.jar"
SENTISTRENGHT_DIR = "../resources/sentstrength_data/"

# NLU Server
NLU_SERVER = "http://localhost:5000"

# NLU Parser parameters
MIN_THRESHOLD = 0.30

# List of intents
INTENT_FINDNEWSCONTENT = 'findNewsContent'
INTENT_ADDCONTENTITEMTOCOLLECTION = 'addContentItemToCollection'
INTENT_BOOKMARKCONTENTITEM = 'bookmarkContentItem'
INTENT_EMAILCONTENTITEM = 'emailContentItem'
INTENT_FAVORITECONTENTITEM = 'favoriteContentItem'
INTENT_GETCONTENTINFO = 'getContentInfo'
INTENT_LISTENPODCAST = 'listenPodcast'
INTENT_RATECONTENTITEM = 'rateContentItem'
INTENT_READARTICLE = 'readArticle'
INTENT_SHARECONTENTITEM = 'shareContentItem'
INTENT_WATCHVIDEO = 'watchVideo'


# List of entities
ENTITY_FINDNEWSCONTENT_AUTHORNAME = 'findnewscontent_authorname'
ENTITY_FINDNEWSCONTENT_CONTENTITEMNAME = 'findnewscontent_contentitemname'
ENTITY_FINDNEWSCONTENT_CONTENTTYPE = 'findnewscontent_contenttype'
ENTITY_FINDNEWSCONTENT_EVENTNAME = 'findnewscontent_eventname'
ENTITY_FINDNEWSCONTENT_LOCATIONNAME = 'findnewscontent_locationname'
ENTITY_FINDNEWSCONTENT_ORGNAME = 'findnewscontent_orgname'
ENTITY_FINDNEWSCONTENT_PERSONNAME = 'findnewscontent_personname'
ENTITY_FINDNEWSCONTENT_SPATIALRELATION = 'findnewscontent_spatialrelation'
ENTITY_FINDNEWSCONTENT_TIMEFRAME = 'findnewscontent_timeframe'
ENTITY_FINDNEWSCONTENT_TOPICNAME = 'findnewscontent_topicname'

ENTITY_ADDCONTENTITEMTOCOLLECTION_COLLECTIONNAME = 'addcontentitemtocollection_collectionname'
ENTITY_ADDCONTENTITEMTOCOLLECTION_CONTENTITEMNAME = 'addcontentitemtocollection_contentitemname'
ENTITY_ADDCONTENTITEMTOCOLLECTION_CONTENTTYPE = 'addcontentitemtocollection_contenttype'

ENTITY_BOOKMARKCONTENTITEM_CONTENTITEMNAME = 'bookmarkcontentitem_contentitemname'
ENTITY_BOOKMARKCONTENTITEM_CONTENTTYPE = 'bookmarkcontentitem_contenttype'
ENTITY_BOOKMARKCONTENTITEM_SELECTCRITERIA = 'bookmarkcontentitem_selectcriteria'

ENTITY_EMAILCONTENTITEM_CONTENTITEMNAME = 'emailcontentitem_contentitemname'
ENTITY_EMAILCONTENTITEM_CONTENTTYPE = 'emailcontentitem_contenttype'
ENTITY_EMAILCONTENTITEM_RECEIPENT = 'emailcontentitem_receipent'
ENTITY_EMAILCONTENTITEM_SELECTCRITERIA = 'emailcontentitem_selectcriteria'

ENTITY_FAVORITECONTENTITEM_CONTENTITEMNAME = 'favoritecontentitem_contentitemname'
ENTITY_FAVORITECONTENTITEM_CONTENTTYPE = 'favoritecontentitem_contenttype'
ENTITY_FAVORITECONTENTITEM_SELECTCRITERIA = 'favoritecontentitem_selectcriteria'

ENTITY_GETCONTENTINFO_CONTENTTYPE = 'getcontentinfo_contenttype'
ENTITY_GETCONTENTINFO_SELECTCRITERIA = 'getcontentinfo_selectcriteria'

ENTITY_LISTENPODCAST_COMMAND = 'listenpodcast_command'
ENTITY_LISTENPODCAST_CONTENTITEMNAME = 'listenpodcast_contentitemname'
ENTITY_LISTENPODCAST_CONTENTTYPE = 'listenpodcast_contenttype'
ENTITY_LISTENPODCAST_SELECTCRITERIA = 'listenpodcast_selectcriteria'

ENTITY_RATECONTENTITEM_CONTENTITEMNAME = 'ratecontentitem_contentitemname'
ENTITY_RATECONTENTITEM_CONTENTTYPE = 'ratecontentitem_contenttype'
ENTITY_RATECONTENTITEM_RATINGVALUE = 'ratecontentitem_ratingvalue'

ENTITY_READARTICLE_COMMAND = 'readarticle_command'
ENTITY_READARTICLE_CONTENTITEMNAME = 'readarticle_contentitemname'
ENTITY_READARTICLE_CONTENTTYPE = 'readarticle_contenttype'
ENTITY_READARTICLE_SELECTCRITERIA = 'readarticle_selectcriteria'

ENTITY_SHARECONTENTITEM_CONTENTITEMNAME = 'sharecontentitem_contentitemname'
ENTITY_SHARECONTENTITEM_CONTENTTYPE = 'sharecontentitem_contenttype'
ENTITY_SHARECONTENTITEM_SOCIALNETWORK = 'sharecontentitem_socialnetwork'

ENTITY_WATCHVIDEO_COMMAND = 'watchvideo_command'
ENTITY_WATCHVIDEO_CONTENTITEMNAME = 'watchvideo_contentitemname'
ENTITY_WATCHVIDEO_CONTENTTYPE = 'watchvideo_contenttype'
ENTITY_WATCHVIDEO_SELECTCRITERIA = 'watchvideo_selectcriteria'
