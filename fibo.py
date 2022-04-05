# Otro programita de python
#Los primeros 10 numeros de la serie de Fibonacci

print("Hola soy Negris2016")
print("")
print("Sigo jugando con las ramas")
print("")
print("Agrego un script nuevo")
print("")

print("Serie de Fibonacci")
print("")

#Program to generate the Fibonacci Sequence till n
n=int(input("Enter the value of 'n': "))

#first two terms are first and second
first=0
second=1

sum=0
count=1

print("Fibonacci Sequence: ")

# Count should not be more then n.
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second

#Fuente: https://conpilar.es/3-formas-de-generar-la-secuencia-de-fibonacci-en-python/