import sys

n, k = map(int, sys.stdin.readline().split())

ix = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    ix += k - 1
    if ix >= len(queue):
        ix %= len(queue)
    res.append(str(queue.pop(ix)))

print("<", ", ".join(res), ">", sep="")