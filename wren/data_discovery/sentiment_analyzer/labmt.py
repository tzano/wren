import subprocess, shlex
from labMTsimple.storyLab import *


class LabMT():
	"""
	Class to interact with LabMT

	Paper The language-dependent relationship between word happiness and frequency
	http://www.pnas.org/content/112/23/E2983.full.pdf

	Credit http://labmt-simple.readthedocs.io/labMTsimple.html
	"""

	def __init__(self, lang='en'):
		"""
		Initialize the class with the language

		:param lang: a text to be analyzed
		:type lang: :py:class:`str`
		"""
		if lang == 'en':
			self.labMT, self.labMTvector, self.labMTwordList = emotionFileReader(stopval=0.0, lang='english',
																				 returnVector=True)
		elif lang == 'ar':
			self.labMT, self.labMTvector, self.labMTwordList = emotionFileReader(stopval=0.0, lang='arabic',
																				 returnVector=True)

	def score_emotion(self, text, lang='en'):
		"""
		Get sentiment score for a given text text

		:param text: a text to be analyzed
		:type text: :py:class:`str`

		:param lang: a text to be analyzed
		:type lang: :py:class:`str`

		:return: sentiment score 0 and 9
		"""
		valence, fvec = emotion(text, self.labMT, shift=True, happsList=self.labMTvector)
		stoppedVec = stopper(fvec, self.labMTvector, self.labMTwordList, stopVal=1.0)
		valence = emotionV(stoppedVec, self.labMTvector)

		if valence == -1:
			return 0
		else:
			return valence
