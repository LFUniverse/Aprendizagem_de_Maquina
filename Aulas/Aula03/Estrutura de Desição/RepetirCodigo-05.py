a = 1

b = 2

c = 3

print (a == b) #False

print (a == b and a == a) #False

print (a == b or a == a) #True

print (a == a or a == a and a==c) #True

print (a == a and a == a or a==c) #True

print (a == a and a == c or a==a) #True

print (a == c and (a == c or a==a)) #False