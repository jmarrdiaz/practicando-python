lista = ["test", 25, 4.5, "test2"]
lista.append(3)
lista.insert(1, "hola")
lista.remove(25)
print(lista)


tupla = ("maria", "perez", "mperez@example.com")
print(tupla[2])
print(len(tupla))
for t in tupla:
    print(t)
    

diccionario = {'a' : 1, 'b' : "test", 'c' : 4.5}
diccionario['a'] = 2
print(list(diccionario.values()))
print(tuple(diccionario.values()))



