import time
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import email
import os


def send_email(file_path, mail_to='2686086371@qq.com'):
    mail_from = '2686086371@qq.com'
    f = open(file_path, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEMultipart()

    # 构造MIMEBase对象作为文件附件内容并添加到根容器
    contype = 'application/octet-stream'
    maintype, subtype = contype.split('/', 1)

    # 读入文件内容并格式化
    data = open(file_path, 'rb')
    file_msg = MIMEBase(maintype, subtype)
    file_msg.set_payload(data.read())
    data.close()

    encoders.encode_base64(file_msg)

    # 设置附件头
    basename = os.path.basename(file_path)
    file_msg.add_header('Content-Disposition', 'attachment', filename=basename)
    msg.attach(file_msg)
    print(u'msg 附件添加成功')

    msg1 = MIMEText(mail_body, "html", "utf-8")
    msg.attach(msg1)

    if isinstance(mail_to, str):
        msg['To'] = mail_to
    else:
        msg['To'] = ','.join(mail_to)
    msg['From'] = mail_from
    msg['Subject'] = u"DOM系统自动化功能测试"
    msg['date'] = time.strftime("%Y-%m-%d-%H-%M-%S")
    print(msg['date'])

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('2686086371@qq.com', 'eelezcxcylijdecj')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')












