# ASCII 97 ~ 122 : a to z
#print('a')
#print(ord('a'))
#print(chr(97))

from string import ascii_lowercase

# 변수 선언
alphabetIndex = [-1]*26
alphabets = list(ascii_lowercase)
word = list(input())

# alphabetIndex 의 요소가 -1 인 요소에 대해서 갱신작업을 진행함으로써
# word 의 중복되는 영문자의 위치에 매우 엄격하게 논리적 대응이 가능
for i in range(len(alphabets)):
    for j in range(len(word)):
        if alphabets[i] == word[j]:
            if alphabetIndex[i] == -1:
                alphabetIndex[i] = j
            else:
                continue

# 출력
for x in range(26):
    print(alphabetIndex[x], end=' ')