from flask import render_template, request
from goguma import goguma
from hoe import Hoe

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
        
