'''
Задача 16. Требуется вычислить, сколько раз встречается 
некоторое число X в массиве A[1..N]. Пользователь в 
первой строке вводит натуральное число N – количество 
элементов в массиве. В последующих строках записаны N 
целых чисел Ai. Последняя строка содержит число X.
5
1 2 3 4 5
3
-> 1
'''

n = int(input('Введите кол-во элементов в массиве: '))
numbers = [int(input("Введите число: ")) for i in range(n)]
print(numbers)

x = int(input("Введите искомое число: "))
count = 0
for i in numbers :
    if i == x :
        count +=1
print(f"число {x} встречается {count} раз")