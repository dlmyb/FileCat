# -*- coding:utf-8 -*-
__author__ = 'calculusma'


def sendemail(name,code,TO):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    me = 'noreply@dlmyb.com'
    you = TO
    passwd = 'Rmbbkb12'
    host = 'smtp.exmail.qq.com'
    msg = MIMEMultipart()
    msg['Subject'] = "【测试】"
    msg['From'] = "【马寅彬】"
    msg['To'] = you
    text = """
    【测试】文件名为%s,提取码是%s,有效期为 72 小时
    """ % (name, code)
    msg.attach(MIMEText(text,"text-plain",'utf-8'))
    s = smtplib.SMTP_SSL()
    s.connect(host,465)
    s.login(me,passwd)
    s.sendmail(me,you,msg.as_string())
    s.quit()
    print 'Send to %s mail Successfully!'%you