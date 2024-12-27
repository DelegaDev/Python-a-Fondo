### OPERADORES ###

# 1. Realiza las siguientes operaciones aritméticas:
print (15 + 25)
print (50 - 22)
print (8 * 7)
print (int (100 / 20)) # He forzado el tipo de dato a entero para que no muestre decimales.

# 2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprí­melo.

remainder = 37 % 5
print (remainder)

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase 'es mi nÃºmero favorito'. Imprime el resultado.

print ( str(7) + ' es mi número favorito')

# 4. Repite la palabra 'Python' 10 veces usando el operador de multiplicación para cadenas y luego imprí­mela.

print ('Python ' * 10)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.

a = 12
b = 8 
resultado = a > b
print ( resultado)

# 6. Compara dos cadenas de texto (apple y banana) usando los operadores > y < y explica cuál tiene mayor orden alfabético.

print ('#6A', 'apple' > 'banana') # El resultado será False porque la 'b' es mayor que la 'a' en el orden alfabético.
print ('#6B', 'apple' < 'banana') # El resultado será True. 

# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.

print ('#7', 10 > 5 and 10 < 20) # El resultado será True porque cumple las dos condiciones.

# 8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.

print ('#8', 7 < 3 or 7 > 5) # El resultado será True porque cumple una de las condiciones.

# 9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?

print ('#9', not 15 > 20) # El resultado será True porque 'not' niega el resultado de la comparación.

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.

print ('#10', ((5*3) + 2) > 10 and ((5*3) +2 ) < 20) # El resultado es True porque cumple las dos condiciones.