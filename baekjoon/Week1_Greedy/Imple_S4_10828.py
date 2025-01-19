## 10828

import sys

num_req = int(sys.stdin.readline())

s = []

for i in range(num_req):
    req = sys.stdin.readline().split()
    if req[0] == 'push':
        s.append(req[1])
    elif req[0] == 'pop':
        if len(s) > 0:
            print(s.pop())
        else:
            print(-1)
    elif req[0] == 'size':
        print(len(s))
    elif req[0] == 'empty':
        if len(s) > 0:
            print(0)
        else:
            print(1)
    elif req[0] == 'top':
        if len(s) > 0:
            print(s[-1])
        else:
            print(-1)