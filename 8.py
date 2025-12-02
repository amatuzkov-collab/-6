first=[0]
mas=[x for x in range(201)]
k=int(input())
if k>=11:
    if k%2!=0:
        print(mas[10+k//4]//10)
    else:
        print(mas[10+k//4]%10)
else:
    print(mas[k-1])
    
    
