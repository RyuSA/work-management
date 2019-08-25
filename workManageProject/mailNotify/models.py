from django.db import models

# Create your models here.


class MailAddress(models.Model):
    """
    メールアドレスクラス
    """
    ADDRESS_TYPE = (
        ('送信先', 'TO'),
        ('個別送信先', 'CC'),
        ('リコンサイル用', 'BCC')
    )
    address = models.CharField(max_length=255)
    address_type = models.CharField(max_length=255, choices=ADDRESS_TYPE)


class Mail(models.Model):
    """
    メール本文クラス
    """
    MAIL_TYPE = (
        ('遅刻', 'DELAY'),
        ('休暇(午前)', 'MORNING_OFF'),
        ('休暇(午後)', 'NIGHT_OFF'),
        ('休暇', 'WHOLE_OFF'),
        ('その他', 'OTHER'),
    )
    address_to = models.ManyToManyField(to=MailAddress)
    mail_type = models.CharField(max_length=255, choices=MAIL_TYPE)
    date = models.DateTimeField(verbose_name='勤怠日時')
    created_at = models.DateTimeField(auto_now_add=True)


class OtherDetail(models.Model):
    """
    「その他」のメールタイプの場合の詳細部分
    """
    mail = models.OneToOneField(to=Mail, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255)


class MailComment(models.Model):
    """
    メールにコメントが必要な場合
    """
    mail = models.OneToOneField(to=Mail, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
