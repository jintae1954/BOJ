# 변수 선언
N = int(input())
S = []

# list 단위로 S에 추가
for n in range(N):
    S.append(list(map(int, input().split())))

# 정렬 규칙
S.sort(key=lambda x: (x[0], x[1]))

# 출력
for s in S:
    print(*s)