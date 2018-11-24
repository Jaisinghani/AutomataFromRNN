import random

chars = 'etaoinsmpru'
#num = int(input('How long do you want the string to be?  '))
#How long do you want the string to be?  10
word_list=[]
number=[3,4,5,6,7]

for num in number:
	for i in range(50):
		str = []
		for k in range(1, num+1):
			str.append(random.choice(chars))
		str = "".join(str)
		word_list.append(str)
print(word_list)
