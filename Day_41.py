import sys

# 변수선언
N = int(sys.stdin.readline())
N_list = [0] * 10001

# index 별로 카운트
for i in range(N):
    N_list[int(sys.stdin.readline())] += 1

# index를 크기 순으로 출력
for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]): #중복까지 출력 가능
            print(i)