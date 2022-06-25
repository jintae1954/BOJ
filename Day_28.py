rows, cols = map(int, input().split())

a,b = [], []

for i in [a, b]: # 빈 리스트 각각에 대하여
  for j in range(rows): # 행의 갯수 만큼
    i.append(list(map(int, input().split()))) # 이중리스트를 빈 리스트에 추가

for i in range(rows):
  for j in range(cols):
    a[i][j] += b[i][j]
  
  print(*a[i]) # 행단위로 출력
