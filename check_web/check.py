# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import hashlib
import os
import time



def getHash(f):
    line = f.readline()
    hash = hashlib.md5()
    while (line):
        hash.update(line)
        line = f.readline()
    return hash.hexdigest()


def IsHashEqual(f1, f2):
    str1 = getHash(f1)
    str2 = getHash(f2)
    return str1 == str2


if __name__ == '__main__':
    # os.system('cd check_web')
    os.system('scrapy crawl check_web_sprider')
    print '0s'
    time.sleep(10)
    print '10s'
    f1 = open("./test.json", "rb")
    f2 = open("./test1.json", "rb")
    print 'testttttweffwfwfwafwfffewttt'

    if (IsHashEqual(f1, f2) is False):
        print IsHashEqual(f1, f2)
        print 'cuocuocuocucoucou cuocuocuocuo cuo'
        def _format_addr(s):
            name, addr = parseaddr(s)
            return formataddr(( \
                Header(name, 'utf-8').encode(), \
                addr.encode('utf-8') if isinstance(addr, unicode) else addr))


        from_addr = 'mclaren1234@163.com'
        password = 'ly19940306'
        to_addr = '342447974@qq.com'
        smtp_server = 'smtp.163.com'

        msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
        msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
        msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
        msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
