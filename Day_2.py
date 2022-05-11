x = list(map(int, input().split()))

#print(x[0])
#print(x[1])
#print(x[2])
#print(x[3])
#print(x[4])

d5_sq = int(x[0])**2
#print(d5_sq)

d4_sq = int(x[1])**2
#print(d4_sq)

d3_sq = int(x[2])**2
#print(d3_sq)

d2_sq = int(x[3])**2
#print(d2_sq)

d1_sq = int(x[4])**2
#print(d1_sq)

y = int((d5_sq + d4_sq + d3_sq + d2_sq + d1_sq) % 10)
print(y)