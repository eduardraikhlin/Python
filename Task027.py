'''
Задача 27. Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
'''

text = "She sells seashells on the sea shore The shells \
that she sells are seashells I'm sure. So if she sells \
seashells on the seashore I'm sure that the shells are \
seashore shells"
print(text)

my_list = text.upper().split()

long = set(my_list)
print(long)
print(len(long))