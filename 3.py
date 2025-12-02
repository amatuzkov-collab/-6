n,m=map(int,input().split('x'))
k=int(input())
#Проверяем можно ли отделить r строк:
#K должно делиться на m, и r должно быть меньше n
flag=False
if k%m==0:
    strok=k//m
    if strok>0 and strok<n:
        flag=True
#Проверяем можно ли отделить r столбцов:
#K должно делиться на n, и r должно быть меньше m
if k%n==0:
    stolb=k//n
    if stolb>0 and stolb<m:
        flag=True
if flag:
    print('да')
else:
    print('нет')
