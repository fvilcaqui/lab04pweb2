from interper import draw
from chessPictures import *

#En esta variable guardamos la ficha de square inverso el cual sera la casilla pero de color negro
Invertido = square.negative()
#En esta variables guardaremos la union del cuadro negro y blanco
PrimeraParte = Invertido.join(square)
#En esta variable guardamos la variable PrimeraParte cuatro veces
Repetido = PrimeraParte.horizontalRepeat(4)
#Guardaremos el valor de la variable Repetido en la variable dibFinal
dibFinal = Picture(Repetido.img)
#Imprimire ambas filas
draw(dibFinal)