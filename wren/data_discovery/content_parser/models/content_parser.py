from abc import ABCMeta, abstractmethod
from os.path import join, dirname, abspath

# Handle library reorganisation Python 2 > Python 3.
try:
	from urllib.parse import urljoin
	from urllib.parse import urlencode
except ImportError:
	from urlparse import urljoin
	from urllib import urlencode

import requests


class ContentParser():
	"""
	Content Parser class
	"""
	__metaclass__ = ABCMeta

	def __init__(self, api_key=None, lang='English'):
		"""
		Initialize the class with api_key and language.

		:param api_key: API Key to access to the service
		:type api_key: :py:class:`str`

		:param lang: the supported language
		:type lang: :py:class:`str`

		"""
		self.api_key = api_key
		self.lang = lang

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
			response = requests.get(
				url, headers=queryparams['headers'], params=queryparams['params'])

			return response

		except requests.exceptions.RequestException as e:
			raise Exception(
				'Invalid API server response.\n%s' % response)

	def _post(self, url, **queryparams):
		"""
		Handle authenticated POST requests

		:param url: The url for the endpoint including path parameters
		:type url: :py:class:`str`

		:param queryparams: The query string parameters
		:type queryparams: :py:class:`dict`

		:returns: The Reponse from the API
		"""
		try:
			if queryparams.get('data', None) != None:
				response = requests.post(url, headers=self._headers, data=queryparams.get('data'))
			else:
				response = requests.post(url, headers=self._headers)

			return response

		except requests.exceptions.RequestException as e:
			raise Exception(
				'Invalid API server response.\n%s' % response)

	def _delete(self, url, supported_versions, data=None):
		"""
		Handle authenticated DELETE requests

		:param url: The url for the endpoint including path parameters
		:type url: :py:class:`str`

		:param queryparams: The query string parameters
		:type queryparams: :py:class:`dict`

		:returns: The Reponse from the API
		"""
		try:
			if data != None:
				response = requests.delete(
					url, headers=self._headers, json=data)
			else:
				response = requests.delete(url, headers=self._headers)

			return response

		except requests.exceptions.RequestException as e:
			raise Exception(
				'Invalid API server response.\n%s' % response)

	def _patch(self, url, supported_versions, data=None):
		"""
		Handle authenticated PATCH requests

		:param url: The url for the endpoint including path parameters
		:type url: :py:class:`str`

		:param queryparams: The query string parameters
		:type queryparams: :py:class:`dict`

		:returns: The Reponse from the API
		"""
		try:
			response = requests.patch(
				url, headers=self._headers, json=data)
			return response

		except requests.exceptions.RequestException as e:
			raise Exception(
				'Invalid API server response.\n%s' % response)

		return None

	def _put(self, url, supported_versions, data=None):
		"""
		Handle authenticated PUT requests

		:param url: The url for the endpoint including path parameters
		:type url: :py:class:`str`

		:param queryparams: The query string parameters
		:type queryparams: :py:class:`dict`

		:returns: The Reponse from the API
		"""

		try:
			response = requests.put(url, headers=self._headers, data=data.encode('utf-8'))
			return response

		except requests.exceptions.RequestException as e:
			raise Exception(
				'Invalid API server response.\n%s' % response.text)

	def fetch(self, text):
		"""
		fetch the web service

		:param text: text to be analyzed
		:type text: :py:class:`str`

		:return:
		"""
		raise NotImplementedError()

	def process_results(self, results):
		"""
		process the results obtained from the webservice

		:param results: a list of entities with metadata from the webservice
		:type results: :py:class:`list`

		:return: processed results
		"""
		raise NotImplementedError()

	def extract_entities(self, entry):
		"""
		extract entities from text

		:param text: text to be analyzed
		:type text: :py:class:`str`

		:return: entities
		"""
		raise NotImplementedError()
