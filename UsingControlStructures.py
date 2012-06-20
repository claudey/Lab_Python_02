theInput = raw_input("Enter an integer: ")
intInput = int(theInput)
if intInput % 2 == 0:
    print "The number you entered is even"
else:
    print "The number you entered is odd"

print "\n-----------------------------------------\n"

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

print "\n-----------------------------------------\n"

i = 40
if i % 3 !=0:
    i=i-1
if i % 3 !=0:
    i=i-1
while i % 3 == 0 and i >= 0:
    print i
    i -= 3

print "\n-----------------------------------------\n"

i = 6
while  i < 30:
    i += 1
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        print i

print "\n-----------------------------------------\n"

n = 1
x = 79
while n > 0:    
    n += 1
    x = 79 * n
    if x % 97 == 1:
        print "The number is",n
        break

