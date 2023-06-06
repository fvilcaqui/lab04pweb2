from interper import draw
from chessPictures import *

#En esta variable guardamos la ficha de square junto a su inverso
PrimeraParte = square.join(square.negative())
#En esta variable guardamos la variable PrimeraParte cuatro veces
Repetido = PrimeraParte.horizontalRepeat(4)

#En esta variable guardamos el inverso de la ficha square, osea el cuadro de color negro
Invertido = square.negative()
#En la variable SegundaParte guardaremos la union de la ficha negra junto a la ficha blanca
SegundaParte = Invertido.join(square)
#En esta variable guardamos la variable SegundaParte cuatro veces
Repetido2 = SegundaParte.horizontalRepeat(4)
#Guardare ambos valores de variables en la variable dibFinal y lo imprimiremos para abajo
dibFinal3 = Picture(Repetido.img + Repetido2.img).verticalRepeat(2)

draw(dibFinal3)