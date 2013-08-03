#!/usr/bin/env python
from hoe.tasks import add
from hoe.tasks import save_png
from hoe.tasks import get_png

result = add.delay(4,4)

print result.get()

print 'get png'
result = get_png.delay('http://google.co.kr')
print result.get()

print 'save png'
save_png.apply(args=('http://google.co.kr', './google.html'))
