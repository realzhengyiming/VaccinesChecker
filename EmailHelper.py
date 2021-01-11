import smtplib
from email.mime.text import MIMEText

from settings import Email_Adress


class EMail(object):
    def __init__(self):
        self.sender_user = Email_Adress['sender_user']
        self.receivers = Email_Adress['receivers']
        self.sender_password = Email_Adress['sender_password']

    def send_email(self, subject: str, message: str):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = self.sender_user
        msg["To"] = ";".join(self.receivers)

        try:
            sender = smtplib.SMTP_SSL(Email_Adress['host'], Email_Adress['port'])
            sender.login(self.sender_user, self.sender_password)
            sender.sendmail(self.sender_user, self.receivers, msg.as_string())
            sender.quit()
            print('Sended!')
        except smtplib.SMTPException:
            print('Falied!')


email_helper = EMail()

if __name__ == '__main__':
    text = "🆕网址 {url} 有更新"
    email = EMail()

    email.send_email(subject="你好，靓仔", message=text)
