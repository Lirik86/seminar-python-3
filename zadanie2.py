import random

n = int(input("Введите кол-во элементов в массиве: "))
list_1 = [0]*n
x = int (input('Введите число х: '))
for i in range(n):
    list_1[i] = random.randint(0,10)
print(f"Массив А: {list_1}")
min = abs(x - list_1[0])
index = 0
for i in range(1, n):
    count = abs(x - list_1[i])
    if count < min:
        min = count
        index = i
print(f'Число {list_1[index]} в списке A наиболее близко по величине к числу {x}, их разница составляет {abs(x - list_1[index])}')