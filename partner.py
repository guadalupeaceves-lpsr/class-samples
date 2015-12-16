

friends = ['Kimberly', 'Giselle','Lady','Melissa','Samuel']
family = ['Mom','Dad','Utsha','Angela','Rosa']
print("Here are the 5 friends and family I spend the most time with:")
total = (friends + family)
total.sort()
total.reverse()
i = 1
for people in total:
    i = i + 1
    print(str(i) + ". " + people)




