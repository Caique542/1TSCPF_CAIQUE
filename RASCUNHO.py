palavra = "Janaina"

print("For")
for i in range (1,11):
    print(i, palavra)

print("While")
i = 1
while i <= 10:
    print(i, palavra)
    i = i + 1

print("Fibo")
numero_termos = int(input("Entre com o numero de termos:"))
a = 0
b = 1
print(a)
print(b)
i = 1
while i <= numero_termos - 2:
    #print(i, palavra)
    c = a + b
    print(c)
    a = b
    b = c
    i = i + 1
