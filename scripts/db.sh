db="<name_of_db>"
use $db

db.articles.createIndex({"news_media_org":1})
db.articles.ensureIndex( {"article_url": 1 }, { unique: true } )

# create indexes for text search
db.articles.createIndex({'article_headline': 'text', 'summary': 'text', 'article_content': 'text'})
db.podcasts.createIndex({'podcast_headline': 'text', 'summary': 'text', 'podcast_content': 'text'})
db.videos.createIndex({'video_headline': 'text', 'summary': 'text', 'video_content': 'text'})