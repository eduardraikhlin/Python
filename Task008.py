'''
Задача 8. Требуется определить, можно ли от шоколадки 
размером n × m долек отломить k долек, если разрешается 
сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
3 2 4 -> yes
3 2 1 -> no
'''

n = int(input('Введите размерность n шоколадки: '))
m = int(input('Введите размерность m шоколадки: '))
k = int(input('Количество отломанных долек: '))

if k < m * n and (k % n == 0 or k % m == 0):
    print('Yes')
else:
    print('No')