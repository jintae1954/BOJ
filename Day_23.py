str_ = list(input())

for i in range(len(str_)):
    #print(str_[i])
    if(str_[i].isupper()):
        str_[i] = str_[i].lower()
    else:
        str_[i] = str_[i].upper()

for i in str_:
  print(i, end='')