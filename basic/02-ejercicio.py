# REORDENANDO NUMEROS:
# a. Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe 
# imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido 
# es el 4532 por pantalla deberá imprimirse:
# 4
# 5
# 3
# 2


number = input("give me a number: ")  # 6532 [1,2,3,4,5]
# for num in number:
#     print(num)


# forloop (iteración infinita hasta que le digamos que se detenga)


# b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que 
# resulta de leer el número introducido de derecha a izquierda. Por ejemplo si el número introducido 
# es 4532, el output deberá ser 2354

# lista
numbers_separates = [1,2,3,4]

# i es el número (ITERAR)
for i in number:
    numbers_separates.append(i) # agregando valior a la lista llamada numbers_separates

x = len(numbers_separates) # devueve el número de elementos que tenga la lista

# forloop de final hacia el inicio
number_reverse = []
while x > 0:
    number_reverse.append(numbers_separates[x - 1])
    x = x - 1

print("".join(number_reverse)) # une los valores de la lista

