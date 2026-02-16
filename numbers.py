count = int(input())
a = input().split(" ")
for i in range(count):
    for j in range(count):
        if a[j-1] > a[j]:
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            
            
print(a)
