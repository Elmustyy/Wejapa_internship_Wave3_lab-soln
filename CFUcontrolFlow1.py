#Question: What type of loop should we use?
#You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.


#we woukd use the for loop inorder give limit to our loop

## Please use this space to test and run your code
odd_num = [x for x in num_list if x%2 !=0]
print('list of  odd numbers on the list:{}\n'.format(odd_num))
#adding the odd_num
sum=0
for num in odd_num[:5]:
	sum += num
	print(sum)