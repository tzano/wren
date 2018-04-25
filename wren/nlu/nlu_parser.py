import os
import requests
from resources.constants import MIN_THRESHOLD

class NLUParser():
    def __init__(self, nlu_server, project_name= 'default', model_name='default'):
        """
        :param nlu_server: the address of the server
        :type nlu_server: :py:class:`str`
        """
        self.nlu_server = nlu_server
        self.model_name = model_name
        self.project_name = project_name

    def _get(self, url, **queryparams):
        """
        Handle authenticated POST requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`

        :param queryparams: The query string parameters
        :type queryparams: :py:class:`dict`

        :returns: The Reponse from the API
        """
        try:
            if None != queryparams.get('data', None):
                response = requests.get(url, params=queryparams.get('data'))
            return response

        except requests.exceptions.RequestException as e:
            raise Exception(
                'Invalid API server response.\n%s' % response)

    def parse(self, message):
        """
        parsing the message to get intent of the user
        :param message: message from client to be parsed
        :type message: :py:class:`str`
        """
        response = self._get("{}/parse".format(self.nlu_server), data={"q": message, "project": self.project_name, "model": self.model_name})
        parsed_data = response.json()

        if parsed_data['intent']['confidence'] < MIN_THRESHOLD:
            intent = None
            entities = []
        else:
            intent = parsed_data['intent']['name']
            entities = parsed_data['entities']

        return intent, entities