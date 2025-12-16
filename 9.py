x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

dx = x1 - x2
dy = y1 - y2
d2 = dx*dx + dy*dy          # d^2

sumR = r1 + r2
diffR = abs(r1 - r2)
sumR2 = sumR ** 2         # (R1+R2)^2
diffR2 = diffR ** 2      # (|R1-R2|)^2

if d2 > sumR2:
    print("Вне, не касаясь")
elif d2 == sumR2:
    print("Внешнее касание")
elif d2 == diffR2:
    print("Внутреннее касание")
elif d2 < diffR2:
    print("Одна внутри другой, не касаясь")
else:
    print("Пересекаются")
