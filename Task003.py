'''
Задача 3. В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32
'''

a = int(input('Количество учеников в первом классе: '))
b = int(input('Количество учеников во втором классе: '))
c = int(input('Количество учеников в третьем классе: '))

res = (a + 1)//2 + (b + 1)//2 + (c + 1)//2
print(res)