from flask import render_template, request, Response
from web.goguma import goguma
from hoe.tasks import get_png
#from hoe import Hoe
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
import json

@goguma.route('/')
def index():
    return render_template('index.html')

@goguma.route('/pagetree', methods=["POST"])
def pagetree():
    input_url = request.form['url']
    return render_template('pagetree.html', url=input_url)


class PageGenNamespace(BaseNamespace):
    def recv_connect(self):
        goguma.logger.info("Client connected")

    def on_pageimg_ask(self, url):
        goguma.logger.info("Client connected")
        src = 'data:image/png;base64,' + get_png.delay(url).get()

        self.emit('pageimg_rep', json.dumps({
            'id': 'a0',
            'url': '/',
            'src': src,
        }))
        self.emit('pageimg_rep', json.dumps({
            'id': 'a1',
            'url': '/teach',
            'src': src,
            'parentid': 'a0'
        }))
        self.emit('pageimg_rep', json.dumps({
            'id': 'a2',
            'url': '/learn',
            'src': src,
            'parentid': 'a0'
        }))
        self.emit('pageimg_rep', json.dumps({
            'id': 'a3',
            'url': '/learn/course',
            'src': src,
            'parentid': 'a2'
        }))
        self.emit('pageimg_rep', json.dumps({
            'id': 'a4',
            'url': '/learn/course',
            'src': src,
            'parentid': 'a3'
        }))

@goguma.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/pagegen': PageGenNamespace}, request)
    except:
        goguma.logger.error("Exception while socketio connection",
                            exc_info=True)
    return Response()
