import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from workManageProject import sercret


class MailSender:

    mail_format = """
    お疲れ様です。{name}です。
    下記の通り勤怠を申請します。

    ---
    {date}
    {mail_type}
    その他: {other}

    よろしくお願いします。
    """

    def construct_mail(self):
        """
        メールを作成する
        """
        msg = MIMEText(self.mail_format)
        msg['Subject'] = "【勤怠報告】"
        msg['From'] = sercret.FROM_ADDRESS
        msg['To'] = sercret.TO_ADDRESS
        msg['Bcc'] = sercret.BCC
        msg['Date'] = formatdate()
        return msg


    def send(self):
        """
        メールを送信
        """
        msg = self.construct_mail()
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
        smtpobj.login(sercret.FROM_ADDRESS, sercret.MY_PASSWORD)
        smtpobj.sendmail(sercret.FROM_ADDRESS, sercret.TO_ADDRESS, msg.as_string())
        smtpobj.close()

