# for
'''
for i in range(1,101):
    print(i)
'''
'''
i = 1
while i < 101:
    print(i)
    i += 1
'''

def imprimirNumero (num):
    if num < 101:
        print(num)
        num +=1
        imprimirNumero(num)
    else:
        return

    
imprimirNumero(1)
