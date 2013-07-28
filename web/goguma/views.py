from flask import render_template, request, Response
from goguma import goguma
from hoe import Hoe
from socketio import socketio_manage
from socketio.namespace import BaseNamespace

@goguma.route('/')
def index():
    return render_template('index.html')

@goguma.route('/url', methods=['POST'])
def maketree():
    input_url = request.form['url']
    template = '''
        <html><head></head>
        <body>
        <img alt='page view' src='data:image/png;base64,%s'/>
        </body>
        </html>
        '''
    with Hoe() as hoe:
        hoe.open(input_url)
        html = template % hoe.get_base64_image()
        return html

class PageGenNamespace(BaseNamespace):
    def recv_connect(self):
        pass

@goguma.route('/socket.io/<path:remaining>')
def socketio(remaining):
    try:
        socketio_manage(request.environ, {'/pagegen': PageGenNamespace}, request)
    except:
        goguma.logger.error("Exception while socketio connection",
                            exc_info=True)
    return Response()


