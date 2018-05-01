import logging
from threading import Thread
import yaml
from resources.constants import CONFIG_DIR, APP_KEYS_FILE, SLACK_SERVICE, SLACK_API_KEY, SLACK_BOT_NAME, \
    SLACK_CHANNEL_NAME, MESSAGING_FILE, NLU_SERVER
from conversations.slack import SlackHandler
import time
from nlu.nlu_parser import NLUParser
from actions.request_handler import RequestHandler
from threading import Thread


class Dialog(Thread):
    """

    // InteractionHandler handles interactive message response.

    """

    def __init__(self, db_connector, db_config, email_config, socialmedia_config):
        """

        :param db_config:
        :param db_connector:
        """
        super(Dialog, self).__init__()
        self.sleep_status = False
        self.active_status = False
        self.request_handler = RequestHandler(db_connector = db_connector, db_config = db_config, socialmedia_config = socialmedia_config)  # init with the right credentials

    def close(self):
        """
        close
        :return:
        """
        return self.sleep_status

    def sleep(self):
        """
        sleep
        :return:
        """
        self.sleep_status = True
        logging.info("Sleep")
        return self

    def quit(self):
        """
        quit
        :return:
        """
        self.active_status = True
        logging.info("Quit")

    def stringify(self, data):
        """
        stringify json output

        :param data:
        :return:
        """
        answer = ""
        for i, item in enumerate(data["articles"]):
            if i == 0:
                answer = "🗞️ 🗞️ 🗞️ \n"
            answer += "📰 *{}*\n 📅 `{}`\n {}\n 🔗 {}\n".format(
                item["article_headline"], item["pub_date"], item["summary"], item["article_url"])
            answer += "\n\n"
        for i, item in enumerate(data["podcasts"]):
            if i == 0:
                answer += "📻 📻 📻\n"
            answer += "🎧 *{}*\n 📅 `{}`\n  ```{}```\n 🔗 {}\n".format(
                item["title"], item["pub_date"], item["summary"], item["podcast_url"])
            answer += "\n\n"
        for i, item in enumerate(data["videos"]):
            if i == 0:
                answer += "📀 📀 📀 \n"
            answer += "📺 *{}*\n 📅 `{}`\n  ```{}```\n 🔗 {}\n".format(
                item["title"], item["pub_date"], item["summary"], item["video_url"])

        return answer

    def run(self):
        """
        run the thread
        """

        slack_config = yaml.load(open("{}/{}".format(CONFIG_DIR, MESSAGING_FILE)))
        app_keys = yaml.load(open("{}/{}".format(CONFIG_DIR, APP_KEYS_FILE)))

        slack_handler = SlackHandler(access_token=slack_config.get(SLACK_SERVICE).get(SLACK_API_KEY),
                                     bot_name=slack_config.get(SLACK_SERVICE).get(SLACK_BOT_NAME),
                                     channel_name=slack_config.get(SLACK_SERVICE).get(SLACK_CHANNEL_NAME))
        nlu_parser = NLUParser(NLU_SERVER)

        if slack_handler.slack_client.rtm_connect():
            while True:
                query = slack_handler.slack_client.rtm_read()
                if len(query) > 0:
                    query = query[0]
                    if query.get('type') == 'message':
                        query_text = query.get('text', "")
                        if query_text != "":
                            intent, entities = nlu_parser.parse(query_text)
                            query_result = self.request_handler.handle_request(intent, entities)

                            if query_result['status'] == 'ok':
                                query_answer = self.stringify(query_result)
                                slack_handler.post(query_answer)

                time.sleep(5)
        else:
            logging.warn("Connection with Slack Failed")
