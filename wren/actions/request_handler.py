from resources.constants import *
from actions.news_quester import NewsQuester
from actions.email_manager import EmailManager
from actions.newsmedia_manager import NewsMediaManager


class RequestHandler(NewsQuester, NewsMediaManager): # add: EmailManager
    def __init__(self, db_connector, db_config, socialmedia_config):
        super(RequestHandler, self).__init__(db_connector=db_connector,
                                             db_config=db_config,
                                             socialmedia_config=socialmedia_config)

    def handle_request(self, intent, entities):
        """
        handle request given that we identified intent, entities

        :return: json file
            {"status": ..,
            "video": .. ,
            "podcasts": ..,
            "articles": ..}
        """
        if intent is not None:
            if intent == INTENT_FINDNEWSCONTENT:
                return self.find_news_content(intent, entities)

            # intent: add_content_item_to_collection
            elif intent == INTENT_ADDCONTENTITEMTOCOLLECTION:
                return self.add_content_item_to_collection(intent, entities)

            # intent: bookmark_content_item
            elif intent == INTENT_BOOKMARKCONTENTITEM:
                return self.bookmark_content_item(intent, entities)

            # intent: favorite_content_item
            elif intent == INTENT_FAVORITECONTENTITEM:
                return self.favorite_content_item(intent, entities)

            # intent: get_content_info
            elif intent == INTENT_GETCONTENTINFO:
                return self.get_content_info(intent, entities)

            # intent: rate_content_item
            elif intent == INTENT_RATECONTENTITEM:
                return self.rate_content_item(intent, entities)

            # intent: email_content_item
            elif intent == INTENT_EMAILCONTENTITEM:
                return self.email_content_item(intent, entities)

            # intent: share_content_item
            elif intent == INTENT_SHARECONTENTITEM:
                return self.share_content_item(intent, entities)

            # intent: listen_podcast
            elif intent == INTENT_LISTENPODCAST:
                return self.listen_podcast(intent, entities)

            # intent: read_article
            elif intent == INTENT_READARTICLE:
                return self.read_article(intent, entities)

            # intent: watch_video
            elif intent == INTENT_WATCHVIDEO:
                return self.watch_video(intent, entities)

    def find_news_content(self, intent, entities):
        """
        parse find_news_content intent
        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        if intent == INTENT_FINDNEWSCONTENT:
            entities = {entity.get("entity"): entity.get("value") for entity in entities}
            contentype_value = None
            # case: filter by type
            if ENTITY_FINDNEWSCONTENT_CONTENTTYPE in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_CONTENTTYPE, None)
                if len(entities) == 1:
                    return self.get_content(contentype_value)

            # case: filter by keyword/event
            if ENTITY_FINDNEWSCONTENT_EVENTNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_EVENTNAME)
                return self.find_content(entity_value, contentype_value)
            # case: filter by author
            if ENTITY_FINDNEWSCONTENT_AUTHORNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_AUTHORNAME)
                return self.filter_content_by_authors([entity_value], contentype_value)
            # case: filter by content item title
            if ENTITY_FINDNEWSCONTENT_CONTENTITEMNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_CONTENTITEMNAME)
                return self.filter_content_by_title(entity_value, contentype_value)
            # case: filter by location name
            if ENTITY_FINDNEWSCONTENT_LOCATIONNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_LOCATIONNAME)
                return self.filter_content_by_location(entity_value, contentype_value)
            # case: filter by org name
            if ENTITY_FINDNEWSCONTENT_ORGNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_ORGNAME)
                return self.filter_content_by_orgname(entity_value, contentype_value)
            # case: filter by person name
            if ENTITY_FINDNEWSCONTENT_PERSONNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_PERSONNAME)
                return self.filter_content_by_person(entity_value, contentype_value)
            # case: filter by time frame
            if ENTITY_FINDNEWSCONTENT_TIMEFRAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_TIMEFRAME)
                return self.filter_content_by_time(entity_value, contentype_value)
            # case: filter by topic
            if ENTITY_FINDNEWSCONTENT_TOPICNAME in entities.keys():
                entity_value = entities.get(ENTITY_FINDNEWSCONTENT_TOPICNAME)
                return self.filter_content_by_topic(entity_value, contentype_value)

            return {"status": "bad"}

    def add_content_item_to_collection(self, intent, entities):
        """
        add content item to collection

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        title = entities[ENTITY_ADDCONTENTITEMTOCOLLECTION_CONTENTITEMNAME]
        content_type = entities[ENTITY_ADDCONTENTITEMTOCOLLECTION_CONTENTTYPE]
        collection_name = entities[ENTITY_ADDCONTENTITEMTOCOLLECTION_COLLECTIONNAME]

        return self.update_content_by_title(title, content_type, collection=collection_name)

    def bookmark_content_item(self, intent, entities):
        """
        bookmark content item

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        title = entities[ENTITY_BOOKMARKCONTENTITEM_CONTENTITEMNAME]
        content_type = entities[ENTITY_BOOKMARKCONTENTITEM_CONTENTTYPE]
        select = entities[ENTITY_BOOKMARKCONTENTITEM_SELECTCRITERIA]

        return self.update_content_by_title(title, content_type, is_bookmarked=True)

    def favorite_content_item(self, intent, entities):
        """
        favorite content item

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        title = entities[ENTITY_FAVORITECONTENTITEM_CONTENTITEMNAME]
        content_type = entities[ENTITY_FAVORITECONTENTITEM_CONTENTTYPE]
        select = entities[ENTITY_FAVORITECONTENTITEM_SELECTCRITERIA]

        return self.update_content_by_title(title, content_type, is_favorite=True)

    def get_content_info(self, intent, entities):
        """
        get content info

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        entity_value = entities[ENTITY_GETCONTENTINFO_CONTENTTYPE]
        return self.filter_content_by_title(entity_value)

    def rate_content_item(self, intent, entities):
        """
        rate content item

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        title = entities[ENTITY_RATECONTENTITEM_CONTENTITEMNAME]
        content_type = entities[ENTITY_RATECONTENTITEM_CONTENTTYPE]
        rating_value = entities[ENTITY_RATECONTENTITEM_RATINGVALUE]

        return self.update_content_by_title(title, content_type, rate=rating_value)

    def email_content_item(self, intent, entities):
        """
        email content item

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        title = entities[ENTITY_EMAILCONTENTITEM_CONTENTITEMNAME]
        content_type = entities[ENTITY_EMAILCONTENTITEM_CONTENTTYPE]
        receiver = entities[ENTITY_EMAILCONTENTITEM_RECEIPENT]

        content = self.set_content(title)
        self.send_email(self, title, content, [receiver])

    def share_content_item(self, intent, entities):
        """
        share content item

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        title = entities[ENTITY_SHARECONTENTITEM_CONTENTITEMNAME]
        content_type = entities[ENTITY_SHARECONTENTITEM_CONTENTTYPE]
        socialmedia_platform = entities[ENTITY_SHARECONTENTITEM_SOCIALNETWORK]

        if socialmedia_platform == 'twitter':
            content = self.set_tweet(title)
            self.share_on_twitter(self, title, content, [receiver])

    def listen_podcast(self, intent, entities):
        """
        listen to podcast

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        command = entities[ENTITY_LISTENPODCAST_COMMAND]
        title = entities[ENTITY_LISTENPODCAST_CONTENTITEMNAME]
        content_type = entities[ENTITY_LISTENPODCAST_CONTENTTYPE]
        select = entities[ENTITY_LISTENPODCAST_SELECTCRITERIA]

        if command == 'start':
            result = self.filter_content_by_title(title, content_type)
            self.start_watching_video(result[0].get("podcast_url"))

    def read_article(self, intent, entities):
        """
        read article

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """

        command = entities[ENTITY_READARTICLE_COMMAND]
        title = entities[ENTITY_READARTICLE_CONTENTITEMNAME]
        content_type = entities[ENTITY_READARTICLE_CONTENTTYPE]
        select = entities[ENTITY_READARTICLE_SELECTCRITERIA]

        if command == 'start':
            result = self.filter_content_by_title(title, content_type)

        self.start_reading_article(title, result["content"])

    def watch_video(self, intent, entities):
        """
        watch video

        :param intent: name of intent
        :type intent: :py:class:`str`

        :param entities: holds all entities
        :type entities: :py:class:`str`

        :return: Json file containing all the items
        """
        command = entities[ENTITY_WATCHVIDEO_COMMAND]
        title = entities[ENTITY_WATCHVIDEO_CONTENTITEMNAME]
        content_type = entities[ENTITY_WATCHVIDEO_CONTENTTYPE]
        select = entities[ENTITY_WATCHVIDEO_SELECTCRITERIA]

        if command == 'start':
            result = self.filter_content_by_title(title, content_type)
            self.start_watching_video(result[0].get("video_url"))
