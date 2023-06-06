from interper import draw
from chessPictures import *

#En esta variable guardamos la ficha de square y su inverso
PrimeraParte = square.join(square.negative())
#En esta variable guardamos la variable PrimeraParte cuatro veces
Repetido = PrimeraParte.horizontalRepeat(4)
#Guardaremos el valor de la variable Repetido la variable dibFinal
dibFinal = Picture(Repetido.img)
#Imprimire ambas filas
draw(dibFinal)
