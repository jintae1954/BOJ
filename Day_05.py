unit_person, area = map(int, input().split())
people = unit_person * area

articles = list(map(int, input().split()))

differences = []

# diff.append(articles[0] - people)
# diff.append(articles[1] - people)
# diff.append(articles[2] - people)
# diff.append(articles[3] - people)
# diff.append(articles[4] - people)

for i in range(5):
  differences.append(articles[i] - people)

for i in range(5):
  print(differences[i], end=' ')
