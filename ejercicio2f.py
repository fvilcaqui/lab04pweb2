from interper import draw
from chessPictures import *

#En esta variable guardamos la ficha de square y su inverso
PrimeraParte = square.join(square.negative())
#En esta variable guardamos la variable PrimeraParte cuatro veces
Repetido = PrimeraParte.horizontalRepeat(4)
#Imprimiremos las fichas
dibFinal1 = Picture(Repetido.img)

#En esta variable guardamos la ficha de square inverso y la ficha escuare normal
Invertido = square.negative()
PrimeraParte2 = Invertido.join(square)
#En esta variable guardamos la variable PrimeraParte cuatro veces
Repetido2 = PrimeraParte2.horizontalRepeat(4)
#Imprimiremos las fichas
dibFinal2 = Picture(Repetido.img)

dibFinal3 = Picture(Repetido.img + Repetido2.img).verticalRepeat(2)

draw(dibFinal3)