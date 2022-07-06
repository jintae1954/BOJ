# 변수 선언
lines = []
vowels = ['a', 'e', 'i', 'o', 'u']

# 테스트 케이스 입력 및  저장
while True:
    line = input()
    line = line.lower()
    lines.append(line)

    if line == '#':
        break

# 모음의 개수 조사 및 출력
for line in lines:
    
    if line == '#':
        break
    
    count = 0
    for i in range(len(line)):
        
        
        if line[i] in vowels:
            count += 1
        
    print(count)
