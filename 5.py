kletki=input()
a,b=kletki.split('-')
stolb1, stolb2, stroka1, stroka2=a[0],b[0],int(a[1]),int(b[1])
stolb_num1=ord(stolb1)-ord('a')+1
stolb_num2=ord(stolb2)-ord('a')+1
if (abs(stolb_num1-stolb_num2)==2 and abs(stroka1-stroka2)==1) or (abs(stolb_num1-stolb_num2)==1 and abs(stroka1-stroka2)==2):
    print('верно')
else:
    print('ошибка')

