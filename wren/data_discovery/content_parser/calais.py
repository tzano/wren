import requests
import logging
from data_discovery.content_parser.models.content_parser import ContentParser


class CalaisAPI(ContentParser):
    """
    Class to interact with OpenClais API endpoints.
    http://www.opencalais.com/
    """
    DEFAULT_API_BASE_URL = "https://api.thomsonreuters.com/permid/calais"

    def __init__(self, api_key=None, lang='English'):
        """
        :param api_key: API Key to access to the service
        :type api_key: :py:class:`str`

        :param lang: the supported language
        :type lang: :py:class:`str`
        """
        self.api_key = api_key
        self.base_url = self.DEFAULT_API_BASE_URL
        self._headers = {'X-AG-Access-Token': self.api_key, 'Content-Type': 'text/raw',
                         'outputformat': 'application/json', 'X-Calais_Language': lang}

    def fetch(self, url, text):
        """
        fetch the web service

        :param text: text to be analyzed
        :type text: :py:class:`str`

        :return:
        """
        try:
            response = requests.post(url, headers=self._headers, data=text.encode('utf-8'))
            return response.json()

        except requests.exceptions.RequestException as e:
            logging.info('Invalid API server response.\n')
            raise e

    def process_results(self, results):
        """
        process the results obtained from the webservice

        :param results: a list of entities with metadata from the webservice
        :type results: :py:class:`list`

        :return: processed results
        """

        filtered_results = []
        for key, entity in results.items():
            try:
                type_group = entity["_typeGroup"]
            except KeyError:
                continue

            if type_group == "socialTag":
                name = entity["name"]
                calais_id = entity["socialTag"]
                score = int(entity["importance"])
                entity_type = ""
                yield {'name': name, 'calais_id': calais_id, 'score': score, 'entity_type': entity_type,
                       'type_group': type_group}

            elif type_group == "topics":
                name = entity["name"]
                calais_id = key
                score = float(entity["score"])
                entity_type = ""
                yield {'name': name, 'calais_id': calais_id, 'score': score, 'entity_type': entity_type,
                       'type_group': type_group}

            elif type_group == "entities":
                name = entity["name"]
                calais_id = key
                score = float(entity["relevance"])
                entity_type = entity.get("_type", "")

                yield {'name': name, 'calais_id': calais_id, 'score': score, 'entity_type': entity_type,
                       'type_group': type_group}


    def extract_entities(self, text):
        """
        extract entities from text

        :param text: text to be analyzed
        :type text: :py:class:`str`

        :return: entities
        """
        results = self.fetch(self.base_url, text)
        return [_ for _ in self.process_results(results)]
