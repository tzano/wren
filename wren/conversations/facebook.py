import requests
import logging
import json

class FacebookMessengerClient():
    """
        The class interfaces facebook's Messenger API
    """
    DEFAULT_ENDPOINT = "https://graph.facebook.com/v2.6/"

    def __init__(self, access_token, verify_token, sensors_collection):
        """
        class to handle operations facebook's Messenger API
        :param access_token: the access token
        :type access_token: :py:class:`str`

        :param verify_token: the verify token to validate the auth
        :type verify_token: :py:class:`str`

        :param sensors_collection: cursor for mongdb collection
        :type sensors_collection: :pymongo:class:`cursor`
        """

        self.access_token = access_token
        self.verify_token = verify_token
        self._params = {"access_token": self.access_token}
        self._headers = {'Content-type': 'application/json'}

    def verify(self, *args, **kwargs):
        """
        verify facebook's Messenger API
        :param args: args
        :type args: :py:class:`dict`

        :param args: kwargs
        :type args: :py:class:`dict`
        """
        if request.args.get('hub.verify_token', '') == self.verify_token:
            return request.args.get('hub.challenge', '')
        else:
            return "Error! Please correct the verify_token"

    def listen(self, data):
        """
        parsing messages we get from FB chatbot
        :param data: data that we get from chat
        :type data: :py:class:`dict`
        """

        if data["object"] == "page":

            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:

                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]
                        recipient_id = messaging_event["recipient"]["id"]
                        message_text = messaging_event["message"]["text"]

                    if messaging_event.get("delivery"):  # delivery confirmation
                        pass

                    if messaging_event.get("optin"):  # optin confirmation
                        pass

                    if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                        pass

    def post(self, recipient, text):
        """Send the message text to recipient with id recipient.

        :param recipient: recipient
        :type recipient: :py:class:`str`

        :param text: text
        :type text: :py:class:`str`
        """

        r = requests.post(self.DEFAULT_ENDPOINT + "/me/messages",
                          params=self._params,
                          data=json.dumps({
                              "recipient": {"id": recipient},
                              "message": {"text": text}
                          }),
                          headers=self._headers)
        if r.status_code != requests.codes.ok:
            logging.info("Message has been sent".format(r.text))


