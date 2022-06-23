while True:
    code = input()
    
    if code=="END":
        break
        
    r_code = code[::-1]
    print(r_code)