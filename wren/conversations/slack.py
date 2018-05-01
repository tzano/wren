from time import sleep
import os
import requests
import logging
from slackclient import SlackClient
import os
import time


class SlackHandler():
    """
    The class interfaces Slack API
    """
    DEFAULT_ENDPOINT = "https://slack.com/api/"

    def __init__(self, access_token, channel_name, bot_name):
        """
        class to handle operations Slack API

        :param access_token: the access token
        :type access_token: :py:class:`str`

        :param channel_name: the channel name
        :type channel_name: :py:class:`str`

        :param bot_name: the name of the bot
        :type bot_name: :py:class:`str`

        """

        self.api_key = access_token
        self.channel = channel_name
        self.bot_name = bot_name
        self._header = {'Content-type': 'application/x-www-form-urlencoded'}
        self.slack_client = SlackClient(self.api_key)

    def post(self, message):
        """
            Send the message text to recipient with id recipient.
        """

        url = "{}{}".format(self.DEFAULT_ENDPOINT, "chat.postMessage")
        r = requests.post(url,
                          headers=self._header,
                          data={"token": self.api_key, "text": message, "as_user": True, "channel": self.channel})
        if r.status_code != requests.codes.ok:
            logging.info("Message has been sent".format(r.text))
        else:
            logging.error("A problem sending a message \n Error: {}".format(r.text))

    def listen(self):
        """
        parsing messages we get from Slack chatbot

        :param data: data that we get from chat
        :type data: :py:class:`dict`
        """

        if self.slack_client.rtm_connect():
            while True:
                time.sleep(1)
        else:
            logging.error("Connection Failed, invalid token?")

