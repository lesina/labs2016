import os
import sys

file = open("output.txt", "w")
if len(sys.argv) == 1:
    file.write("Usage: stat filename\n")
    sys.exit(1)
else:
    try:
        a = open(sys.argv[1], "r")
    except:
        file.write("Can't open file " + sys.argv[1])
        sys.exit(2)
    else:
        file.write(str(os.path.getsize(sys.argv[1])))
        file.close()
        sys.exit(0)
