import math
n,k,m=map(int,input().split())
raz=(math.ceil(n/k))*2 #сколько прокрутов карусели, каждый по 2 раза
time=raz*m
print(time)

