""" Se importa la libreria Random"""
import random
nums = []
print("Genera 10 numeros aleatorios que esten entre 5 y 50")
for _ in range (10):
    randomNum = random.randint(5,50)
    nums.append(randomNum)
print(nums)

print("\nGenera 20 numeros aleatorios que esten entre 0 y 100 que sean pares")
nums2 = []
for _ in range(20):
    """                                                 inicio,final,intervalos """
    randomNum2 = random.randrange(0, 100 , 2)
    nums2.append(randomNum2)
print(nums2)

print("\nGenerar 10 numeros aleatorios multiplos de 5")
nums3 = []
for _ in range (10):
    randomNum3 = random.randint(1,10)*5
    nums3.append(randomNum3)
print (nums3)

print("\nGenerar lista con 20 numeros secuenciales y presentarlo de manera randomized")
nums4 =[]
nums5 = []
print("\nUsando for dentro de la variable")
nums4 = [i for i in range(1,21)]
print(nums4)
random.shuffle(nums4)
print(nums4)
print("\nUsando for normal")
for i in range(1,21):
    nums5.append(i)
print(nums5)
random.shuffle(nums5)
print(nums5)

print("\nUsar numeros aleatorios para escojer un rango de numeros secuenciales 0 y 50")
nums6 = []
rand1 = random.randint(0,50)
rand2 = random.randint(0,50)
if rand1 < rand2:
    for i in range (rand1,rand2+1):
        nums6.append(i)
    print(rand1, rand2)
    print(nums6)
    random.shuffle(nums6)
    print(nums6)
elif rand2 < rand1:
    for i in range (rand2,rand1+1):
        nums6.append(i)
    print(rand1, rand2)
    print(nums6)
    random.shuffle(nums6)
    print(nums6)
else:
    print('Son Iguales rand1{0} y rand2{1}'.format (rand1,rand2))






