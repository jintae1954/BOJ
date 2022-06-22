word = list(str(input()))
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = [0] * 26


for i in range(26):
    for letter in word:
        if alphabets[i] in letter:
            answer[i] = answer[i] + 1
        
    print(answer[i], sep=" ")