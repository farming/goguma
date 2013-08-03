#!/usr/bin/env python
from hoe.tasks import add
from hoe.tasks import save_png
from hoe.tasks import get_png
from hoe.tasks import get_internal_links

result = add.delay(4,4)

print result.get()

print 'get png'
result = get_png.delay('http://google.co.kr')
print result.get()

internal_link_results = get_internal_links.delay('test')
print internal_link_results.get()

print 'save png'
save_png.apply(args=('http://google.co.kr', './google.html'))
