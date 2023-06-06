from interper import draw
from chessPictures import *

# Guardare el caballo junto a su negativo que seria el caballo negro 
fil1 = knight.join(knight.negative())
#En la segunda variable guardare el vertical mirror osea los caballos volteados mirando hacia el otro lado debajo
fil2 = fil1.verticalMirror()
#Guardare ambos valores de variables en la variable dibFinal
dibFinal = Picture(fil1.img + fil2.img)
#Imprimire ambas filas
draw(dibFinal)