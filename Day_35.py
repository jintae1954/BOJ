# 입력변수
N, M = map(int, input().split())
sequences = []

# 입력
for n in range(N):
    sequence = input()
    sequences.append(sequence)

# 입력반전 및 출력
for sequence in sequences:
    
    for m in range(M):
        print(sequence[M-1-m], end='')

    print()