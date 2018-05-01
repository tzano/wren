import subprocess
import pyvona
import yaml
from resources.constants import CONFIG_DIR, APP_KEYS_FILE, VONA_USERNAME, VONA_KEY, TTS_PERONA


class NewsMediaManager():
    def __init__(self, language='en', **kw):
        super(NewsMediaManager,self).__init__()
        self.language = language

    def init_speaker(self, tts_username, tts_key, language='en'):
        """
        set voice

        :param tts_username: username
        :type tts_username: :py:class:`str`

        :param tts_key: key
        :type tts_key: :py:class:`str`

        :return:
        """
        app_keys = yaml.load(open("{}/{}".format(CONFIG_DIR, APP_KEYS_FILE)))
        tts = pyvona.create_voice(app_keys[VONA_USERNAME], app_keys[VONA_KEY])
        tts.voice_name = TTS_PERONA

        return tts

    def start_reading_article(self, title, content):
        """
        start reading article

        :param title: content of the article
        :type title: :py:class:`str`

        :param content: content of the article
        :type content: :py:class:`str`

        :return:
        """
        tts = self.init_speaker()
        tts.speak("Reading article entitled {}".format(title))
        tts.speak(content)

    def start_listening_podcast(self, link):
        """
        start listening to a podcast using vlc

        :param link: link to podcast
        :type link: :py:class:`str`

        :return:
        """
        subprocess.call('vlc {}'.format(link), shell=True)


    def start_watching_video(self, link):
        """
        start watching a video

        :param link: link to video
        :type link: :py:class:`str`

        :return:
        """
        subprocess.call('vlc {}'.format(link), shell=True)

