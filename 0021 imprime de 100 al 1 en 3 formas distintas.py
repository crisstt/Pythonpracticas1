# usando For
n_i = []
for i in range(100, 0, -1):
    n_i.append(i)
print(n_i)
# usando while
n_k = []
k = 100
while k > 0:
    n_k.append(k)
    k -= 1
print(n_k)

# for elegante
list_num = [int(i) for i in range(100,0,-1)]
print(list_num)
