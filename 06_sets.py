### SETS ###
# 1. Crea un set con los números del 1 al 5 e imprímelo.

my_set = {1, 2, 3, 4, 5}
print (type (my_set))
print (my_set)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprímelo.

my_set.add (6)
print (my_set)

# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?

my_set.add (5)
print (my_set)      # No se añade el número 5 nuevamente

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.

my_set = {1, 2, 3, 4, 5}
resultado = 3 in my_set
print(resultado)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.

my_set.remove (4)
print (my_set)

# 6. Usa el método clear() para vaciar un set y luego imprime su longitud.

my_set.clear ()
print (len (my_set))

# 7. Convierte el set {"manzana", "naranja", "plátano"} en una lista e imprime el primer elemento de la lista.

my_set = {"manzana", "naranja", "plátano"}
my_list = list (my_set)
print (my_list [0]) # Cada vez que ejecutas el código el resultado puede variar!!!

# 8. Realiza la unión de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

my_set = {1, 2, 3}
my_other_set = {4, 5, 6}
sum_set = my_other_set.union (my_set)
print (sum_set)

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

set01 = {1, 2, 3, 4}
set02 = {3, 4, 5, 6}
set_rest = set02.difference (set01)
print (set_rest)

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado.

my_set = {1, 2, 3}
del my_set 
print (my_set)      # NameError: name 'my_set' is not defined