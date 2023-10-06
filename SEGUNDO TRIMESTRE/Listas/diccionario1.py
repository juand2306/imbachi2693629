
colores=['blue','amarillo','verde','rojo','negro','blanco','morado','naranja','rosado','cafe']
diccionario={"azul":"blue",
         "amarillo":"yellow",
         "verde":"green",
         "rojo":"red",
         "negro":"black",
         "blanco":"white",
         "morado":"purple",
         "naranja":"orange",
         "rosado":"pink",
         "cafe":"brown"}

for word in colores:
    if word in diccionario:
        print( word,'->', diccionario[word])
    else:
        print(word, "no esta en el diccionario")
        