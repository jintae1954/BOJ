import sys

t1, t2, t3, t4 = map(int, sys.stdin.read().split())

t = t1 + t2 + t3 + t4

m = t // 60
sec = t % 60

print(m)
print(sec)
