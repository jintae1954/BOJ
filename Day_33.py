n = input()
answer = 0

for i in range(len(n)):
    answer += int(n[i])**5

print(answer)