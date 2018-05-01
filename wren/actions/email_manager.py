import smtplib
import getpass
import logging


class EmailManager():
    def __init__(self, email_config):
        """
        """
        self.email_config = email_config

    def send_email(self, title, content, receivers):
        """
        send an email given a title and content of the email

        :param title:
        :type title: :py:class:`str`

        :param content:
        :type content: :py:class:`str`

        :param receivers:
        :type receivers: :py:class:`list`

        :return:
        """
        subject = "[Wren]: {} ".format(title)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        logging.info("Please enter your email password")
        passw = getpass.getpass()
        session.login(self.email_config["sender"], passw)
        headers = "\n".join(["from: " + self.email_config["sender"], "subject: " + subject, "mime-version: 1.0",
                             "content-type: text/html"])
        content = headers + "\n\n" + content
        session.sendmail(self.email_config["sender"], receivers, content)

    def set_content(self, title):
        """
        set content

        :param title:
        :type title: :py:class:`str`

        :return:
        """
        return title
