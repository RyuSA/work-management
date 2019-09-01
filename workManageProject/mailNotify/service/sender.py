import smtplib
from mailNotify.models import Mail
from email.mime.text import MIMEText
from email.utils import formatdate
from workManageProject import sercret
from datetime import datetime

class MailSender:

    mail_format = """
    お疲れ様です。{name}です。
    下記の通り勤怠申請をさせていただきます。
    -----------------------------------------------------------
    【勤怠連絡】
    取得予定日：{date}
            {type}
    休暇区分：  ■休暇 □代休
    休暇理由：{reason}
    -----------------------------------------------------------
    よろしくお願いいたします。
    """

    def construct_mail(self, mail: Mail):
        msg = MIMEText(self.mail_format)
        msg['Subject'] = "【勤怠連絡】"
        msg['From'] = sercret.FROM_ADDRESS
        msg['To'] = sercret.TO_ADDRESS
        msg['Bcc'] = sercret.BCC
        msg['Date'] = formatdate()
        return msg

    def construct_msg(self, mail: Mail):
        """
        メールを作成する
        """
        # 遅刻
        if mail.mail_type == Mail.MAIL_TYPE[0][0]:
            pass
        # 休暇(午前)
        elif mail.mail_type == Mail.MAIL_TYPE[1][0]:
            pass
        # 休暇(午後)
        elif mail.mail_type == Mail.MAIL_TYPE[2][0]:
            pass
        # 休暇
        elif mail.mail_type == Mail.MAIL_TYPE[3][0]:
            pass
        # その他
        elif mail.mail_type == Mail.MAIL_TYPE[4][0]:
            pass
        today = datetime.now().strftime("%Y年%m月%d日")
        content = self.mail_format.format(name = "斎藤", date = today, type = "□全休 □午前 □午後 □その他遅刻/早退等（16:00 ～）", reason = "電車遅延のため")
        msg = MIMEText(content)
        msg['Subject'] = "【勤怠連絡】"
        msg['From'] = sercret.FROM_ADDRESS
        msg['To'] = sercret.TO_ADDRESS
        msg['Bcc'] = sercret.BCC
        msg['Date'] = formatdate()
        return msg


    def send(self):
        """
        メールを送信
        """
        mail = Mail()
        mail.mail_type = Mail.MAIL_TYPE[0]
        msg = self.construct_msg(mail)
        smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
        smtpobj.login(sercret.FROM_ADDRESS, sercret.MY_PASSWORD)
        smtpobj.sendmail(sercret.FROM_ADDRESS, sercret.TO_ADDRESS, msg.as_string())
        smtpobj.close()

