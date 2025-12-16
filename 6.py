import math 

N, K, M = map(int, input().split())

sessions = math.ceil(N/K)*2
time = sessions * M

print(time)
