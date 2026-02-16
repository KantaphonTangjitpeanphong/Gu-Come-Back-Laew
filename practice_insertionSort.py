a = input()
initial = a.split(",")
print(initial)

for i in range(len(initial)):
    initial[i] = int(initial[i])

for j in range(1, len(initial)):
    key = initial[i]
    k = j - 1 
    while k >= 0 and key < initial[k]:
        initial[k+1] = initial[k]
        k -= 1
        initial[k+1] = key
print(initial)