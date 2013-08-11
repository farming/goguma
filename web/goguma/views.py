from flask import render_template, request, Response
from web.goguma import goguma
from hoe.tasks import get_png, get_internal_links
#from hoe import Hoe
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from gevent import Greenlet
import hashlib
import time
import json

@goguma.route('/')
def index():
    return render_template('index.html')

@goguma.route('/pagetree', methods=["POST"])
def pagetree():
    input_url = request.form['url']
    return render_template('pagetree.html', url=input_url)


class PageGenNamespace(BaseNamespace):
    max_depth = 2
    def work_on_url(self, input_url, parent_id, current_depth):
        hasher = hashlib.md5()
        hasher.update(input_url)
        hasher.update('%s' % round(time.time() * 1000))
        current_id = hasher.hexdigest()

        Greenlet.spawn(self.pageimg_req, input_url, current_id, parent_id)
        Greenlet.spawn(self.pagelink_req, input_url, current_id, current_depth)

    def pageimg_req(self, input_url, current_id, parent_id):
        src = 'data:image/png;base64,' + get_png.delay(input_url).get()
        self.emit('pageimg_rep', json.dumps({
            'id': current_id,
            'url': input_url,
            'src': src,
            'parentid': parent_id
        }))
    
    def pagelink_req(self, input_url, current_id, current_depth):
        if current_depth > self.max_depth:
            return
        link_list = get_internal_links.delay(input_url).get()
        for url in link_list:
            Greenlet.spawn(self.work_on_url, url, current_id, current_depth + 1)

    def recv_connect(self):
        goguma.logger.info("Client connected")

    def on_pageimg_ask(self, input_url):
        goguma.logger.info("Client connected")
        Greenlet.spawn(self.work_on_url, input_url, None, 1)

@goguma.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/pagegen': PageGenNamespace}, request)
    except:
        goguma.logger.error("Exception while socketio connection",
                            exc_info=True)
    return Response()
