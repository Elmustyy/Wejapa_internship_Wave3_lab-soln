#Filter Names by Scores

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [x for x in scores if scores[x]<=65 ]
# write your list comprehension here
print(passed)