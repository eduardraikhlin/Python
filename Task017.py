'''
Задача 17. Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

myList = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(myList)))
print(set(myList))