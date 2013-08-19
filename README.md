goguma
======

Diagnose your website accessibility dramatically

Dependencies
=======

현재 필요한 것
------------------

* python 2.7

### hoe

* phantomjs 1.9.1
  * **MacOS**
    * brew update && brew install phantomjs

    * python selenuim driver.
      * pip install selenium
        * v2.33.0 

        * celery-3.0.21
          * pip install celery

          * BeautifuSoup4
            * pip install beautifulsoup4

            * rabbitmq
              * `brew install rabbitmq` or `sudo apt-get install rabbitmq-server'

              * Korean Font
                * **Ubuntu 13.04**
                  * `apt-get install ttf-nanum` then `sudo fc-cache -fv`

### web server

* flask 설치하기.
  * pip install flask

  * python gevent
    * pip install gevent , 그런데 native code dependency가 있으므로 ubuntu의 경우 다음을 설치해 준다.
      * sudo apt-get install python-dev
        * sudo apt-get install libevent-dev

        * python gevent-socketio
          * pip install gevent-socketio
            * 이것을 사용하면 import socketio가 가능하다.
