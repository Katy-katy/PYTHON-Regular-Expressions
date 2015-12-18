import re

sum = 0
hand = open('regex_sum_166914.txt') 

inp = hand.read()

numbers = re.findall("[0-9]+", inp)

for num in numbers:
		num = int(num)		sum = sum +num
		
print(sum)

