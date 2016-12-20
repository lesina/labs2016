import sys
res = 0
for i in sys.argv:
    try:
        res += int(i)
    except:
        continue
sys.exit(res)
