
from tasks import add
from tasks import save_png

result = add.delay(4,4)

print result.get()

save_png.apply(args=('http://google.co.kr', './google.html'))

