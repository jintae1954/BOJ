# 입력
query = int(input())

# 초기값
a_n = 1
n = 1
i = 0

# 지나는 방의 개수 파악하기
while 1: 
    # 입력이 방  번호 1인 경우는 특수 케이스
    if query == 1: 
        print(1)
        break
    
    # 지나는 방의 개수 출력
    if query <= a_n:
        print(n)
        break
    
    n = n + 1
    i = i + 1 

    a_n = a_n + 6*i # 육각형 방 번호 점화식