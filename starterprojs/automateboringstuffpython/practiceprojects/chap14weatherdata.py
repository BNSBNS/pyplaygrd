import json, requests,sys
from pydoc import locate

if len(sys.argv) < 2:
    print('usage: quick weather py location')
    sys.exit()

location = ' '.join(sys.argv[1:])

