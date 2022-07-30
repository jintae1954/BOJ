# 입력
N = int(input())
x = 0
y = 0

# N = 5x + 3y
while N >= 0:
    if N % 5 == 0:
        x = x + N // 5
        print(x+y)
        break
    
    N = N - 3
    y = y + 1

# N != 5x + 3y
else:
    print(-1)
