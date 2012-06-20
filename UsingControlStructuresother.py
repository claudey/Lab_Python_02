theInput = raw_input("Enter an integer: ")
intInput = int(theInput)
if intInput % 2 == 0:
    print "The number you entered is even"
else:
    print "The number you entered is odd"

"-------------------"

primarySchoolAge = 6
votingAge = 18
presidentAge = raw_input("Please enter the age at which someone becomes a president")
retirementAge = raw_input("Please enter the retirement age")
personsAge = input("Enter an age: ")
intPrimarySchoolAge = int(primarySchoolAge)
intVotingAge = int(votingAge)
intPresidentAge = int(presidentAge)
intRetirementAge = int(retirementAge)
intPersonsAge = int(personsAge)
if intPrimarySchoolAge < 6:
    print "You are too young for school"
elif intVotingAge >= 18:
    print "Remember to vote"
elif intPresidentAge >= 40:
    print "Vote for me"
elif intPresidentAge < 40:
    print "You can't be President"
elif intRetirementAge >=60:
    print "Too old."
