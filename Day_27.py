id_submit = []
check = [0]*30 #전체 학생 30명

# 28명의 학생들의 과제 접수
for i in range(28):
    submit = int(input())
    id_submit.append(submit)

# 과제를 제출한 28명의 학생들 학번 저장
# 학번과 인덱스는 1 만큼 차이. 인덱스 = 학번-1
for id_number in id_submit:
    check[id_number-1] =+ 1
    
#print(check)

# Tip. range(5)은 0,1,2,3,4
# 제출하지 않은 학생들의 학번 출력
for i in range(30):
  if (check[i] == 0):
    print(i+1)