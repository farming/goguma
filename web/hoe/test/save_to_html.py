import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir) 

from backend import Backend

with Backend() as b:
    b.open('http://google.com')
    b.save_to_html('./test.html')
