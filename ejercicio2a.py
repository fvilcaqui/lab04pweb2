from interper import draw
from chessPictures import *

# Guardare el caballo junto a su negativo que seria el caballo negro 
fil1 = knight.join(knight.negative())
# Guardare al inverso de la primera fila osea los colores seran al reves
fil2 = fil1.negative()
# Imprimire ambas filas
dibFinal = Picture(fil1.img + fil2.img)

draw(dibFinal)