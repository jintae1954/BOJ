import sys

# 변수선언
N = int(input())
N_list = []

# 입력
for i in range(N):
    N_list.append(int(sys.stdin.readline()))

# 정렬
N_list.sort()

# 출력
for i in N_list:
    sys.stdout.write(str(i)+'\n')