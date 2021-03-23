# -*- coding:utf-8 -*-
"""
邮件推送模块
"""

import os
import smtplib

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.loggers import LOGGER
from settings import MAIL_CONFIG


class MailPush(object):

    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        邮箱初始化配置
        :param smtp_server: smtp服务器
        :param smtp_port: smtp端口
        :param smtp_user: smtp用户
        :param smtp_password: smtp密码
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    @staticmethod
    def build_mail_object(sender, receiver, subject, body, attachments=[]):
        """
        构建邮件对象（主旨、正文、附件）
        :param sender: 发件人
        :param receiver: 收件人
        :param subject: 邮件主旨
        :param body: 邮件正文（超文本格式）
        :param attachments: 附件列表
        :return: mail obj
        """
        # 构造邮件头信息
        mail_obj = MIMEMultipart('mixed')
        mail_obj['From'] = sender
        mail_obj['To'] = ','.join(receiver) if isinstance(receiver, list) else receiver
        mail_obj['subject'] = Header(subject, 'utf-8')

        # 构造邮件正文（使用超文本格式）
        html_obj = MIMEText(body, 'html', 'utf-8')
        mail_obj.attach(html_obj)

        if attachments:
            # 添加附件到邮件中
            for each_att in attachments:
                if not os.path.exists(each_att):
                    LOGGER.error(f'添加附件失败，请检查文件：（{each_att}），发件人：{sender}，收件人：{receiver}，主旨：{subject}')
                    continue

                att_file = open(each_att, 'rb')
                file_obj = MIMEText(att_file.read(), 'base64', 'utf-8')
                att_file.close()
                file_obj["Content-Type"] = 'application/octet-stream'
                file_obj["Content-Disposition"] = 'attachment;filename="{}"' \
                    .format(Header(os.path.basename(each_att).encode('utf-8'), 'utf-8'))
                mail_obj.attach(file_obj)

                LOGGER.debug(f'添加附件成功，文件：（{each_att}），发件人：{sender}，收件人：{receiver}，主旨：{subject}')
        return mail_obj

    def send_mail(self, sender, receiver, subject, body, attachments=[]):
        """
        发送邮件
        QQ邮箱 smtp_password 获取方式：进入QQ邮箱-设置-账户-开启服务-开启POP3/SMTP服务，然后点击生成授权码
        :param sender: 发件人
        :param receiver: 收件人
        :param subject: 邮件主旨
        :param body: 邮件正文（超文本格式）
        :param attachments: 附件列表
        :return:
        """
        mail_obj = self.build_mail_object(sender, receiver, subject, body, attachments)
        try:
            # 登陆smtp服务器
            sftp_obj = smtplib.SMTP(self.smtp_server, self.smtp_port)
            sftp_obj.login(user=self.smtp_user, password=self.smtp_password)
            # 发送邮件
            sftp_obj.sendmail(sender, receiver, mail_obj.as_string())
            LOGGER.debug(f'发送邮件成功，发件人：{sender}，收件人：{receiver}，主旨：{subject}')
            # 退出登陆
            sftp_obj.quit()
        except Exception as ex:
            LOGGER.error(f'发送邮件失败，错误原因：{ex}，发件人：{sender}，收件人：{receiver}，主旨：{subject}')


MAIL_PUSH = MailPush(MAIL_CONFIG['smtp_server'], MAIL_CONFIG['smtp_port'],
                     MAIL_CONFIG['smtp_user'], MAIL_CONFIG['smtp_password'])


if __name__ == '__main__':
    # 邮件推送测试
    MAIL_PUSH.send_mail(sender=MAIL_CONFIG['sender'], receiver=MAIL_CONFIG['receiver'], subject=MAIL_CONFIG['subject'],
                        body='<p> This is a test <p>', attachments=['temp.txt'])
