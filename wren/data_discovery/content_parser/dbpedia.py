from data_discovery.content_parser.content_parser import ContentParser


class DbpediaAPI(ContentParser):
    """
    Class to interact with DBpedia API endpoints
    http://dbpedia.org
    """

    DBPEDIA_ENDPOINT = "http://lookup.dbpedia.org/api/search.asmx"
    SPOTLIGHT_ENDPOINT = "http://model.dbpedia-spotlight.org/en"
    CONFIDENCE = 0.3

    def __init__(self, api_key=None, lang='English'):
        """
        Keyword is not required 
        :param api_key: API Key to access to the service
        :type api_key: :py:class:`str`

        :param lang: the supported language 
        :type lang: :py:class:`str`


        """
        self.api_key = api_key
        self.base_url = self.DBPEDIA_ENDPOINT
        # self._headers =   { "Accept" : "application/json", "Content-type" : "application/x-www-form-urlencoded;charset=utf-8" }
        self._headers = {"Accept": "application/json"}

    def spotlight_annotate(self, text):
        """
        Querying DBpedia's `Spotlight API <https://github.com/dbpedia-spotlight/dbpedia-spotlight/wiki>`_.

        :param text: text to be analyzed.
        :type text: :py:class:`str`

        :return: DBpedia's JSON response 
        """
        url = "{}/{}".format(self.SPOTLIGHT_ENDPOINT, "annotate")
        params = {"text": text, "confidence": self.CONFIDENCE}
        response = self._get(url=url, params=params, headers=self._headers)

        return response.json()

    def extract_entities(self, text):
        """
        Extracting most releavant entities using DBpedia's `Spotlight API <https://github.com/dbpedia-spotlight/dbpedia-spotlight/wiki>` 
        
        :param text: text to be analyzed.
        :type text: :py:class:`str`

        :return: DBpedia's JSON response 
        """
        results = self.spotlight_annotate(text)
        return [resource.get('@URI') for resource in results['Resources']]

    def dbpedia_keyword_search(self, keyword):
        """
        Querying DBpedia's keyword search API to get matching entities

        :param keyword: Keyword to be used in the query
        :type keyword: :py:class:`str`
        """
        url = "{}/{}".format(self.DBPEDIA_ENDPOINT, "KeywordSearch")
        params = {
            "QueryClass": "",
            "QueryString": keyword
        }
        response = self._get(url=url, params=params, headers=self._headers)

        return response.json()

    def dbpedia_prefix_search(self, prefix):
        """
        Search by word prefix

        :param prefix: prefix to be used in the query
        :type prefix: :py:class:`str`
        """
        url = "{}/{}".format(self.DBPEDIA_ENDPOINT, "PrefixSearch")

        params = {
            "QueryClass": "",
            "QueryString": prefix,
            "MaxHits": 5
        }

        response = self._get(url=url, params=params, headers=self._headers)

        return response.json()
