import math
sree=[int(i) for i in input().split()]
print(int(((sree[0]*sree[1])/(math.gcd(sree[0],sree[1])))))
