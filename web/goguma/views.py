from flask import render_template, request, Response
from goguma import goguma
from hoe import Hoe
from socketio import socketio_manage
from socketio.namespace import BaseNamespace

@goguma.route('/')
def index():
    return render_template('index.html')

@goguma.route('/pagetree', methods=["POST"])
def pagetree():
    input_url = request.form['url']
    return render_template('pagetree.html', url=input_url)


class PageGenNamespace(BaseNamespace):
    def recv_connect(self):
        goguma.logger.info("Client connected");

    def on_pageimg_ask(self, input_url):
        goguma.logger.info("Client connected");
        # Put celery request here!
        with Hoe() as hoe:
            hoe.open(input_url)
            self.emit('pageimg_rep', hoe.get_base64_image());


@goguma.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/pagegen': PageGenNamespace}, request)
    except:
        goguma.logger.error("Exception while socketio connection",
                            exc_info=True)
    return Response()
