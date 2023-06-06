from interper import draw
from chessPictures import *

#En esta variable guardamos la dicha de queen cuatro veces
fil1 = queen.horizontalRepeat(4)
#Guardare el valor de la variable fil1 en la variable dibFinal
dibFinal = Picture(fil1.img)
#Imprimire la primera fila
draw(dibFinal)