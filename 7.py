k=int(input())

flag=False
for x in range(0,100):
    for y in range(0,100):
        if x*5+y*7==k:
            flag=True
            
if flag==True:
    print('да')
else:
    print('нет')
