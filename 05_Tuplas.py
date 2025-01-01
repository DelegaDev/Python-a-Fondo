### TUPLAS ###

# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.

tupla01 = (10, 20, 30, 40, 50)
print (tupla01)
print (type (tupla01))

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

tupla02 = (100, 200, 300, 400, 500)
print (tupla02 [1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

tupla03 = (1, 2, 3)
# tupla03 [0] = 10           # TypeError: 'tuple' object does not support item assignment
print (tupla03)

# 4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

tupla04 = (1, 2, 3, 3, 4, 5, 3)
print (tupla04.count (3))

# 5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

tupla05 = ("Java", "Python", "JavaScript", "Python")
print (tupla05.index ('Python'))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

tupla06_1 = (1, 2, 3)
tupla06_2 = (4, 5, 6)
sum_tuplas = tupla06_1 + tupla06_2
print (sum_tuplas)
print (tupla06_1 + tupla06_2)

# 7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

tupla07 = (10, 20, 30, 40, 50)
print (tupla07 [2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

tupla08 = ("rojo", "verde", "azul")
tupla08 = list (tupla08)
tupla08 [1] = 'amarillo'
tupla08 = tuple (tupla08)
print (tupla08)
print (type (tupla08))
# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

my_tuple = (1, 2, 3)
del my_tuple
# print (my_tuple)      NameError: name 'my_tuple' is not defined

# 10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

tupla10 = (100, )
print (tupla10)
print (type (tupla10))
