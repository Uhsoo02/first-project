n = int(input())

W = []

for i in range(n):
    W.append(int(input()))

d = [0]*n

d[0] = W[0]
if n > 1:
    d[1] = W[0]+W[1]

if n > 2:
    d[2] = max(W[2]+W[1], W[2]+W[0], d[1])

for i in range(3, n):
    d[i] = max(d[i-1], d[i-3]+ W[i-1]+W[i], d[i-2]+W[i])

print(d[n-1])