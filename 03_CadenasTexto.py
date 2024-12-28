# 1. Declara una variable text con la frase 'Aprendiendo Python' y luego imprime la longitud de la cadena usando len().
text = 'Aprendiendo Python'
print ('#1',len (text))

# 2. Concatena dos cadenas: Hola y Python, y muestra el resultado en una sola lí­nea.

print ('#2', 'Hola ' + 'Python')

# 3. Crea una cadena que incluya un salto de lí­nea, y luego imprí­mela para ver el resultado.

print ('#3', 'Me estoy volviendo un \nexperto en Python')

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

nombre = 'Moi'
apellido = 'Myself'
edad = 99
print ('#4', f'mi nombre es {nombre} {apellido} y tengo {edad} años')

# 5. Desempaqueta los caracteres de la palabra Python en variables separadas y luego imprí­melos uno por uno.

descomponer = 'Python'
a, b, c, d, e, f = descomponer
print ('#5', f'\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}')

# 6. Extrae un slice de la palabra Programación para obtener los caracteres desde la posición 3 hasta la 7.

print ('#6', 'Programación'[3:8])

# 7. Invierte la cadena 'Python' usando slicing y muestra el resultado.

print ('#7', 'Python' [::-1])

# 8. Convierte la cadena 'aprendiendo python' en mayúsculas usando el método adecuado e imprí­mela.

print ('#8', 'aprendiendo python'.upper())

# 9. Cuenta cuántas veces aparece la letra 'n' en la cadena 'Programación en Python'.

print ('#9', 'Programación en Python'.count ('n'))

# 10. Verifica si la cadena '12345' es numérica usando el método adecuado e imprime el resultado.

print ('#10', '12345'.isnumeric ())