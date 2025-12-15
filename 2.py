a,b=map(int,input().split("x"))
c,d,e=map(int,input().split('x'))

flag=False
if (c <= a and d <= b) or (c <= b and d <= a):
    flag = True
if (c <= a and e <= b) or (c <= b and e <= a):
    flag = True
if (e <= a and d <= b) or (e <= b and d <= a):
    flag = True

if flag:
    print('да')
else:
    print('нет')
        

