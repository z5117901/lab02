'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and 
sorting them alphanumerically. Suppose the following input is 
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()


# Define this function to return the expected output
# Do not print it from this function
def singlify(sentence):
	
	splits = sentence.split(' ')
	dic = {}
	new_str = []
	for word in splits	:
		temp = word.upper()	
		if temp not in dic:
			dic[temp] = temp
			new_str.append(word)
	new_str.sort()
	
	return ' '.join(new_str)
	
print(singlify(sentence))
