length = int(input())
numbers = list(map(int,input().split()))
target = int(input())

count = 0
for i in range(length):
  if(numbers[i] == target):
    count = count + 1

print(count)