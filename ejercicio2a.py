from interper import draw
from chessPictures import *

# Guardare el caballo junto a su negativo que seria el caballo negro 
fil1 = knight.join(knight.negative())
# Guardare al inverso de la primera fila osea los colores seran al reves
fil2 = fil1.negative()
# Guardaremos ambas imagenes en Picture
dibFinal = fil1.up(fil2)
# Imprimire ambas filas
draw(dibFinal.verticalRepeat(2))