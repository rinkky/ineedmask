import sys
from checker import check_store

if len(sys.argv) > 1:
    check_store.check_forever(False, True)
else:
    check_store.check_forever()
