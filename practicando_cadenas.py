cadena = "Texto de prueba"

cadena2 = "Esto es el numero {} {}" .format("2", 3)
print(cadena2)


cadena3 = "Esto es el print " + "numero 2" + " que sale por pantalla"
print(cadena3)  


aux = "Esto es una cadena de strings" + " con lo cual " + "siempre hay que concatenar strings... si no, hay que usar format"

print (aux)

aux = "Necesito concatenar variables de diferente tipo {} si tengo un uno: {}, o un dos... {}" . format("entonces", 1, 2)
print (aux)