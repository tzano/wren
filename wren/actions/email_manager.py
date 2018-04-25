import smtplib


class EmailManager():
    def __init__(self, credentials):
        self.email_config = credentials

    def send_email(self, title, content, receivers):
        """
        send an email given a title and content of the email
        :param title:
        :param content:
        :param receivers:
        :return:
        """
        subject = "[Wren]: {} ".format(title)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
        session.login(self.email_config["sender"], self.email_config["password"])
        headers = "\n".join(["from: " + self.email_config["sender"], "subject: " + subject, "mime-version: 1.0",
                             "content-type: text/html"])
        content = headers + "\n\n" + content
        session.sendmail(self.email_config["sender"], receivers, content)
