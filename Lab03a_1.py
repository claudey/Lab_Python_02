n = int(raw_input("Enter a number = "))
x = 0
i = 0
number = n
while number >= 10:
  number = number/10
  i += 1
number = n
while number >= 10:
  x = x + (number%10)*10**i
  print (number%10)*10**i
  number = number/10
  i -= 1
else:
  print (number%10)*10**i
  number = x + number
  print 'The reversed number is', number
