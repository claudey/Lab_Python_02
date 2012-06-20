x = raw_input ('x:')
y = raw_input ('y:')
x = int(x)
y = int(y)
z = x+3
if z==1:
    y=0
elif z==2:
    y=10
elif z==4:
    y+=1
else:
    y=1
print "The value of y is",y
