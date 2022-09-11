nameFile = "Novelas_y_fantasías.txt"
group = 3
dictionary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
             "á", "é", "í", "ó", "ú"]


file = open(nameFile, "r", encoding='utf8')
textSplit = file.read().split("   \n    ")## se separa por algo que no exista para dejar una lista de tamaño 1


#Filtrado de datos (eliminar caracteres fuera del diccionario)
for word in range(len(textSplit)):
    textSplit[word] = textSplit[word].lower()
    for char in range(len(textSplit[word])):
        if textSplit[word][char] in dictionary:
            pass
        else:
            textSplit[word] = textSplit[word].replace(textSplit[word][char]," ")


#Separacion del vector por espacios ya que no existen caracteres desconocidos
textSplit = textSplit[0].split(" ")


#Eliminacion de posiciones vacias en el vector
count = 0
for word in range(len(textSplit)):
  if len(textSplit[word]) == 0:
    count += 1
for x in range(count):
  textSplit.remove("")


#Para rellenar y completar el grupo
for word in range(len(textSplit)):
  mod = len(textSplit[word]) % group
  if mod == 0:
    pass
  else:
    add = group - (len(textSplit[word]) % group)
    add = len(textSplit[word]) + add
    textSplit[word] = textSplit[word].ljust(add, ".")


#Para buscar el numero de letra en el diccionario y adjuntarlo al vector salida
out = []
for word in range(len(textSplit)):
  for char in range(len(textSplit[word])):
    if textSplit[word][char] in dictionary:
      out.append(dictionary.index(textSplit[word][char]))
    else:
      out.append(" ")


#Para mirar la letra que pertenece a cada numero
outWord = []
for num in range(len(out)):
  if out[num] == " ":
    outWord.append(" ")
  else:
    outWord.append(dictionary[out[num]])


#imprimir en los grupos configurados (OPCION 1)
# pos = 0
# for num in range(int(len(out)/group)):
#   pos = num * group
#   print(out[pos:pos+group])

#OPCION 2 (MEJOR)
out = [out[i:i + group] for i in range(0, len(out), group)]
outWord = [outWord[i:i + group] for i in range(0, len(outWord), group)]


#visualizacion de los primeros 100 grupos
for i in range(100):
  print(out[i], " --> ", outWord[i])