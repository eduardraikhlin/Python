'''
Задача 21. Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

myList = [{"V":"S001"}, {"V":"S002"}, {"VI":"S001"},
{"VI":"S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

result = []
for item in myList :
    result.append(list(item.values())[0])
print(set(result))