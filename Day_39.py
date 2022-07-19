# 입력
A, B = input().split()

# 입력 뒤집기
A = A[::-1]
B = B[::-1]

# 출력
if A>B:
    print(A)
else:
    print(B)