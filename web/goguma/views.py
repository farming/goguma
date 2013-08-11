from flask import render_template, request, Response
from web.goguma import goguma
from hoe.tasks import get_png, get_internal_links
#from hoe import Hoe
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import Greenlet

@goguma.route('/')
def index():
    return render_template('index.html')

@goguma.route('/pagetree', methods=["POST"])
def pagetree():
    input_url = request.form['url']
    return render_template('pagetree.html', url=input_url)


class PageGenNamespace(BaseNamespace):
    max_depth = 3
    def pageimg_req(self, input_url):
        self.emit('pageimg_rep', get_png.delay(input_url).get())
    
    def pagelink_req(self, input_url, current_depth):
        if current_depth > self.max_depth:
            return
        link_list = get_internal_links.delay(input_url).get()
        for url in link_list:
            Greenlet.spawn(self.pageimg_req, url)
            Greenlet.spawn(self.pagelink_req, url, current_depth + 1)

    def recv_connect(self):
        goguma.logger.info("Client connected")

    def on_pageimg_ask(self, input_url):
        goguma.logger.info("Client connected")
        Greenlet.spawn(self.pageimg_req, input_url)
        Greenlet.spawn(self.pagelink_req, input_url, 1)

@goguma.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/pagegen': PageGenNamespace}, request)
    except:
        goguma.logger.error("Exception while socketio connection",
                            exc_info=True)
    return Response()
