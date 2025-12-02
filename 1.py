r=6.5
A,B=map(int, input().split('x'))
if (A**2 + B**2)**0.5<=2*r:
    print('да')
else:
    print('нет')
