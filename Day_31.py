patient = list(input().split('h'))
doctor = list(input().split('h'))

#print(patient, end=' ')
#print(doctor)

if len(patient[0]) >= len(doctor[0]):
    print('go')
else:
    print('no')