from flask_frozen import Freezer
from goguma import goguma

freezer = Freezer(goguma)

if __name__ == '__main__':
    freezer.freeze()
