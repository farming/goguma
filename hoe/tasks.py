
from celery import Celery
from hoe import Hoe

celery = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

@celery.task
def add(x, y):
    print x
    return x+y

@celery.task
def save_png(url, file_name):
    print 'start extract png.'
    with Hoe() as hoe:
        hoe.open(url)
        hoe.save_to_html(file_name)
    print 'end extract png.'

@celery.task
def get_png(url):
    print 'start extract png.'
    with Hoe() as hoe:
        hoe.open(url)
        return hoe.get_base64_image()
    print 'end extract png.'

@celery.task
def get_internal_links(base_url, url):
    print 'start extract internal url.'
    sub_url_list = hoe.get_sub_url(base_url, url)
    print 'end extract internal url.'
    return sub_url_list
    #return ['http://www.google.co.kr', 'http://www.naver.com', 'http://www.daum.net']
