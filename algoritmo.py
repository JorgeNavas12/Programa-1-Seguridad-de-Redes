nameFile = "entrada.txt"
group = 3
dictionary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "á", "é", "í", "ó", "ú"]




file = open(nameFile, "r")

textSplit = file.read().split("   \n    ")## se separa por algo que no exista para dejar una lista de tamaño 1
print(textSplit)


##FILTRADO DE DATOS
for word in range(len(textSplit)):
    textSplit[word] = textSplit[word].lower()
    for char in range(len(textSplit[word])):
        if textSplit[word][char] in dictionary:
            pass
        else:
            textSplit[word] = textSplit[word].replace(textSplit[word][char]," ")


print(textSplit)

# x = dictionary[0].ljust(15, "x")
# print(x)

textSplit = textSplit[0].split(" ")

##PARA ELIMINAR POSICIONES VACIAS
count = 0
for word in range(len(textSplit)):
  if len(textSplit[word]) == 0:
    count += 1

for x in range(count):
  textSplit.remove("")

print(textSplit)
print(len(textSplit))

#Para rellenar y completar el grupo
for word in range(len(textSplit)):
  mod = len(textSplit[word]) % group
  if mod == 0:
    pass
  else:
    add = group - (len(textSplit[word]) % group)
    add = len(textSplit[word]) + add
    textSplit[word] = textSplit[word].ljust(add, ".")

print(textSplit)
out = []
#Para buscar el numero de letra en el diccionario
for word in range(len(textSplit)):
  for char in range(len(textSplit[word])):
    if textSplit[word][char] in dictionary:
      out.append(dictionary.index(textSplit[word][char]))
    else:
      out.append(" ")

print(out)

#imprimir grupos de 3

pos = 0
for num in range(int(len(out)/group)):
  pos = num * group
  print(out[pos:pos+group])