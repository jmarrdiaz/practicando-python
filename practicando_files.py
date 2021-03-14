file = open("fichero.txt", "w")
content = "Texto en el fichero"
file.write(content)
file.close()


file = open("fichero.txt", "r")
lines = file.readlines()
print(lines)
file.close()


