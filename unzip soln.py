#Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names = [ i for i, j in cast]
heights = [j for i, j in cast]
print(names)
print(heights)