import sys
import os

count = int(sys.argv[1])
if 2 +count > len(sys.argv):
    wall = len(sys.argv)
else:
    wall = 2+count
for i in range(2, wall):
    print(sys.argv[i], os.environ[sys.argv[i]], sep="=")
