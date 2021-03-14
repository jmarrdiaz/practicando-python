words = ["test", 2, "aux"]

for word in words:
    if word == "test":
        continue
    print(word)

words.append(3)
print(words)

for i in range(2):
    print(i)

for j in range(2,4):
    print(j)


edad = 70

if (edad > 12 and edad < 18):
    print("adolescente")
elif (edad >= 18 and edad < 65):
    print("adulto")
else:
    print("mayor")
    