# boj 4999
patient = list(input().split('h'))
doctor = list(input().split('h'))

#print(patient, end=' ')
#print(doctor)

if len(patient[0]) >= len(doctor[0]):
    print('go')
else:
    print('no')
    
    
# boj 9086    
cases = int(input())
case = 0

while case < cases:
    case += 1
    string = input()
    print('{}{}'.format(string[0], string[-1]))
