songs, avg = map(int, input().split())

qtyMel = songs * (avg -1)
min_qtyMel = qtyMel + 1

print(min_qtyMel)
