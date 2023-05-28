import random

n = int(input("Введите кол-во элементов в массиве: "))
list_1 = [0]*n
x = int (input('Введите число х: '))
count = 0
for i in range(n):
    list_1[i] = random.randint(0,10)
for i in range(n):
    if list_1[i] == x:
        count += 1
print(f"Массив А: {list_1}")
print(f'Число {x} встречается в списке А {count} раз.')