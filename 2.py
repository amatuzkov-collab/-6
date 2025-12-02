a,b=map(int,input().split("x"))
c,d,e=map(int,input().split('x'))
#создаем массивы с размерами граней дыры и кирпича
kirp=[c,d,e]
dirka=[a,b]
#создаем массив с размерами всех сторон кирпича
storoni=[(kirp[0],kirp[1]),(kirp[0],kirp[2]),(kirp[1],kirp[2])]
flag=False
#Проверяем все пары сторон кирпича, может ли кирпич пройти в дыру
for x,y in storoni:
    if (x<=dirka[0] and y<=dirka[1]) or (x<=dirka[1] and y<=dirka[0]):
        flag=True
        break
if flag:
    print('да')
else:
    print('нет')
        
