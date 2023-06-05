from interper import draw
from chessPictures import *

#En esta variable guardamos la ficha de square inverso y la ficha escuare normal
Invertido = square.negative()
PrimeraParte = Invertido.join(square)
#En esta variable guardamos la variable PrimeraParte cuatro veces
Repetido = PrimeraParte.horizontalRepeat(4)
#Imprimiremos las fichas
dibFinal = Picture(Repetido.img)
draw(dibFinal)