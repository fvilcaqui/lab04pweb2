from interper import draw
from chessPictures import *

#En esta variable guardamos la dicha de queen cuatro veces
fil1 = queen.horizontalRepeat(4)
#Imprimiremos las fichas correspondientes
dibFinal = Picture(fil1.img)

draw(dibFinal)