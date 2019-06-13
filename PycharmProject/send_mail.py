import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'PycharmProject.settings'

if __name__ == '__main__':

    subject,from_email,to = '来自www.choujuhua.com的测试邮件','zqb19930208@sina.com','1454094633@qq.com'
    text_content='欢迎访问www.choujuhua.com,这里是刘江的博客与教学站点，专注Python和Django技术的分享！'
    html_content='<p>欢迎访问<a href="http://www.choujuhua.com" target=blank>www.choujuhua.com</a>,这里是刘江博客和教程站点！</p>'
    msg=EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,"text/html")
    msg.send()