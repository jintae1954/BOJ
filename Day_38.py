# 입력 및 변수선언
a = input().upper()
word = list(set(a)) # set 자료형으로 중복 제거
cnt = [] # 세아린 알파벳 개수를 담을 리스트

# 알파벳 개수 세아리기
for i in word:
    count = a.count(i)
    cnt.append(count)
                    
if cnt.count(max(cnt)) >= 2: # 세아린 알파벳 리스트에 대하여 중복 확인
    print("?")
else:
    print(word[cnt.index(max(cnt))])