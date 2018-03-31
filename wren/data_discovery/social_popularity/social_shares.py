import requests
import json


class SocialShares:
    FB_URL = "http://graph.facebook.com/?id="
    REDDIT_URL = "https://www.reddit.com/api/info.json?limit=100&url="
    GOOGLE_PLUS_URL = "https://clients6.google.com/rpc?key="
    TWITTER_URL = "http://cdn.api.twitter.com/1/urls/count.json?url="
    PINTEREST_URL = "http://api.pinterest.com/v1/urls/count.json?url="
    STUMBLEUPON_URL = "http://www.stumbleupon.com/services/1.01/badge.getinfo?url="
    ADDTHIS_URL = "http://api-public.addthis.com/url/shares.json?url="
    LINKEDIN_URL = "https://www.linkedin.com/countserv/count/share?url="

    def __init__(self, api_keys=None):
        """
        Initialize the class with api_keys, a dictionary that holds all the social platform keys

        :param api_keys: API Keys to access to social platforms
        :type api_keys: :py:class:`dict`
        """
        self.api_keys = api_keys

    def _get(self, url, **queryparams):
        """
        Handle authenticated GET requests

        :param url: The url for the endpoint including path parameters
        :type url: :py:class:`str`

        :param queryparams: The query string parameters
        :type queryparams: :py:class:`dict`

        :returns: The Reponse from the API
        """
        try:
            response = requests.get(url, timeout=5)

            return response

        except requests.exceptions.RequestException as e:
            raise Exception(
                'Invalid API server response.\n%s' % e)

    def _remove_params(self, url):
        if url.find('?') == -1:
            return url
        else:
            return url[:url.find('?')]

    def get_twitter_shares(self, url):
        """
        Return the number of times a given URL had been tweeted.

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on
        """
        # raise NotImplementedError()

        endpoint = "{}{}".format(self.TWITTER_URL, self._remove_params(url))
        response = self._get(url=endpoint)

        return response.json()['count']

    def get_fb_shares(self, url):
        """
        Return the number of times a given URL had been shared on FB.

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on FB
        """
        endpoint = "{}{}".format(self.FB_URL, self._remove_params(url))
        response = self._get(url=endpoint)

        return response.json().get(u'share', {}).get(u'share_count')

    def get_fb_comments(self, url):
        """
        Return the number of times a given URL had been commented on FB.

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of comments on FB
        """
        endpoint = "{}{}".format(self.FB_URL, self._remove_params(url))
        response = self._get(url=endpoint)

        return response.json().get(u'share', {}).get(u'comment_count')

    def get_fb_likes(self, url):
        """
        Return the number of times a given URL had been liked on FB.
        This method need auth (FB key)

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of likes on FB
        """
        raise NotImplementedError()

    def get_google_plus_shares(self, url):
        """
        Return the number of times a given URL had been shared on Google.

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on Google
        """
        endpoint = "{}{}".format(self.REDDIT_URL, self._remove_params(url))
        response = self._get(url=endpoint)

        content = response.json()

    def get_reddit_shares(self, url):
        """
        Return the number of times a given URL had been shared on Google.

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on
        """
        endpoint = "{}{}".format(self.REDDIT_URL, self._remove_params(url))
        response = self._get(url=endpoint)

        response_json = response.json()

        nbr_mentions = sum((child['data'] or {'score': 0})['score'] for child in response_json[u'data']['children'])

        return nbr_mentions

    def get_stumbles(self, url):
        """
        Return the number of times a given URL was viewed in StumbleUpon

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on StumbleUpon
        """
        endpoint = "{}{}".format(self.STUMBLEUPON_URL, self._remove_params(url))
        response = self._get(url=endpoint)

        return response.json().get('result', {}).get('views')

    def get_pins(self, url):
        """
        Return the number of times a given URL has been pinned in Pinterest

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on
        """
        endpoint = "{}{}".format(self.PINTEREST_URL, self._remove_params(url))
        response = self._get(url=endpoint)
        return json.loads(response.text.split("receiveCount(", 1)[1].split(")", 1)[0])['count']

    def get_linkedin_shares(self, url):
        """
        Return the number of times a given URL has been shared on Linkedin

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on Linkedin
        """
        endpoint = "{}{}&format=json".format(self.LINKEDIN_URL, self._remove_params(url))
        response = self._get(url=endpoint)
        return response.json().get(u'count')

    def get_social_media_shares(self, url):
        """
        Return the number of times a given URL has been shared on social media platforms

        :param url: a link to the article
        :type url: :py:class:`str`

        :return: a number of shares on Social Media Platforms
        """
        return {"Reddit": self.get_reddit_shares(url)}
