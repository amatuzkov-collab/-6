klet=input()
stolb=klet[0]
stroka=int(klet[1])
#найдем числовое значение номера столбца, где орд а это номер "a" в
#системе питона
stolb_num=ord(stolb)-ord('a')+1
if (stolb_num+stroka)%2==0: #a1 - сумма столбца и клетки 1+1=2 и она черная
    print('чёрный')
else:
    print('белый')
