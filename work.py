import sys 
people = sys.argv[1]
donuts = sys.argv[2]
peopleOne = int(people)
peopleone = str(peopleOne)
donutsOne = int(donuts)
donutsone = str(donutsOne)
answer = peopleOne // donutsOne
answer1 = str(answer)
print("Our party has" + " " + peopleone + " " + "people" + " " + "and" + " " + donutsone + ".")
print("Each person at the party gets" + " " + answer1 + " " + "donuts.")
