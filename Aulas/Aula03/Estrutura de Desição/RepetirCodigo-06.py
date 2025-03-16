a = 1

b = 2

c = 3

if (a == b): 
    print ("Primeiro teste é verdadeiro.")

if (a == b and a == a): 
    print ("Segundo teste é verdadeiro.")

if (a == b or a == a):
    print ("Terceiro teste é verdadeiro.")

if (a == a or a == a and a==c):
    print ("Quarto teste é verdadeiro.")

if (a == a and a == a or a==c):
    print ("Quinto teste é verdadeiro.")

if (a == a and a == c or a==a):
    print ("Sexto teste é verdadeiro.")

if (a == c and (a == c or a==a)):
    print ("Sétimo teste é verdadeiro.")

print ("Saindo do IF.")