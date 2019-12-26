#!/usr/bin/python
import random
word = "Hello"
word2 = "Python"
word3 = "world!"
data = word
data2 = word2

class AI:
	def __init__(self):
		firstWord = ""
		secondWord = ""
	def train(self, data, count, selected_word):
		stuff = ""
		while stuff != selected_word:
			stuff = ""
			for i in range(count):
				for char in random.choice(data):
					stuff += char
				print(stuff)
				if len(stuff) != len(selected_word):
					print("\r")
				if selected_word == stuff:
					print("Word Found!")
					return stuff
		
barry = AI()
#firstWord = barry.train(data,len(word), word)
#secondWord = barry.train(data2,len(word2), word2)
#thirdWord = barry.train(word3, len(word3), word3)
string = "Your Text Here for The ML to Copy"

arrayedString = string.split(' ')
i = 0
for word in arrayedString:
	arrayedString[i] = barry.train(word, len(word), word)
	i += 1
print("\n")
string2 = ""
for word in arrayedString:
	#if word == arrayedString[0]:
		#print(word + " " + arrayedString[1] + " " + arrayedString[2] + arrayedString[3])
		#exit(0)
	string2 += word + " "
print(string2)
