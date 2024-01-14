# import the whole system library
import sys

if len(sys.argv) != 2:
    print('Missing command line arguments')
    sys.exit(0)
else:
    print(f"{sys.argv[1]}")