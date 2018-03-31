import subprocess, shlex


class SentiStrength():
    """
    Class to interact with SentiStrength
    http://sentistrength.wlv.ac.uk/
    Credit http://sentistrength.wlv.ac.uk/documentation/Python.txt 
    """
    SentiStrength_ENDPOINT = 'http://sentistrength.wlv.ac.uk/results.php'

    def __init__(self, jar_path="../resources/SentiStrength.jar", dir_path="../resources/sentstrength_data/"):
        self.jar_path = jar_path
        self.dir_path = dir_path

    def score_sentiment(self, text):
        """
        Get sentiment score for a given text text

        :param text: a text to be analyzed
        :type text: :py:class:`str`

        :return: sentiment score -5 -> 1-5
        """
        text = text.replace(" ", "+").encode('utf8')
        p = subprocess.Popen(shlex.split("java -jar {} stdin sentidata {}".format(self.jar_path, self.dir_path)),
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_text, stderr_text = p.communicate(text)
        stdout_text = stdout_text.decode().rstrip().replace("\t", "")
        return stdout_text
