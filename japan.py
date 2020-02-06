# я знаю, что это ебаный костыль.
# до ума можно довести, добавив проверку на самое длинное слово
# чтобы останавливать лупу не через 15 циклов
# а через количество букв в самом длинном слове

import sys

message = sys.argv[1]

data = message.split()

i = 0
j = 15

while j > 0:
	for word in data:
		if i < len(word):
			print(word[i] + " ", end='')
		else:
			print("  ", end='')
	print('')
	i = i + 1
	j = j - 1
