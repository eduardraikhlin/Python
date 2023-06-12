'''
Задача 35. Напишите функцию, которая принимает 
одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''

number = int(input("Введите число"))
def is_simple(number) :
    if number > 2 and number % 2 != 0 :
        for i in range(3, number // 2) :
            if number % i == 0:
                return False
        return True
    return False
print(is_simple(number))