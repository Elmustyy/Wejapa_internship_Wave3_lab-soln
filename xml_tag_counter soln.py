#Tag Counter
#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in tokens:
	if i[0].startswith('<') and i[-1].endswith('>'):
		count +=1
		

print(count)