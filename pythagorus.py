import math
n = input()
a = n.split(" ") 
a[0] = int(a[0]) **2
a[1] = int(a[1]) **2
print("{:.6f}".format(math.sqrt(a[0]+a[1])))

