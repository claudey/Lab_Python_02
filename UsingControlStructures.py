theInput = raw_input("Enter an integer: ")
intInput = int(theInput)
if intInput % 2 == 0:
    print "The number you entered is even"
else:
    print "The number you entered is odd"

"-------------------"

primarySchoolAge = 6
votingAge = 18
presidentAge = 40
retirementAge = 60
personsAge = input("Enter an age: ")
intPersonsAge = int(personsAge)
if intPersonsAge < primarySchoolAge:
    print "You are too young for school"
if intPersonsAge >= votingAge:
    print "Remember to vote"
if intPersonsAge >= presidentAge:
    print "Vote for me"
if intPersonsAge < presidentAge:
    print "You can't be President"
if intPersonsAge >= retirementAge:
    print "Too old."
