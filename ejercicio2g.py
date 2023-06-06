from interper import draw
from chessPictures import *

# Preparamos todas las piezas en su versión negativa osea de color negro
torreNegra = rock.negative()
caballoNegro = knight.negative()
alfilNegro = bishop.negative()
reynaNegra = queen.negative()
reyNegro = king.negative()
peonNegro = pawn.negative()
cuadradoNegro = square.negative()

# Posicionamos todas las fichas negras en distintos cuadrados ; CO = Cuadro Oscuro - CC = Cuadro Claro
torreNegraCC = square.under(torreNegra)
caballoNegroCC = square.under(caballoNegro)
alfilNegroCC = square.under(alfilNegro)
peonNegroCC = square.under(peonNegro)
torreNegraCO = cuadradoNegro.under(torreNegra)
caballoNegroCO = cuadradoNegro.under(caballoNegro)
alfilNegroCO = cuadradoNegro.under(alfilNegro)
peonNegroCO = cuadradoNegro.under(peonNegro)
reynaNegra = cuadradoNegro.under(reynaNegra)
reyNegro = (square).under(reyNegro)
reyna = (square).under(queen)
rey = cuadradoNegro.under(king)

# Posicionamos todas las fichas blancas en distintos cuadrados ; CO = Cuadro Oscuro - CC = Cuadro Claro
torreCC = square.under(rock)
caballoCC = square.under(knight)
alfilCC = square.under(bishop)
peonCC = square.under(pawn)
torreCO = cuadradoNegro.under(rock)
caballoCO = cuadradoNegro.under(knight)
alfilCO = cuadradoNegro.under(bishop)
peonCO = cuadradoNegro.under(pawn)

#Guardamos los valores de las filas vacias
filaVaciaBlanco = (square.join(cuadradoNegro)).horizontalRepeat(4)
filaVaciaNegro = (cuadradoNegro.join(square)).horizontalRepeat(4)

# En las siguientes lineas de código se genera cada una de las filas del tablero
fila1 = torreNegraCC.join(caballoNegroCO).join(alfilNegroCC).join(reynaNegra).join(reyNegro).join(alfilNegroCO).join(caballoNegroCC).join(torreNegraCO)
fila2 = (peonNegroCO.join(peonNegroCC)).horizontalRepeat(4)
fila7 = (peonCC.join(peonCO)).horizontalRepeat(4)
fila8 = torreCO.join(caballoCC).join(alfilCO).join(rey).join(reyna).join(alfilCC).join(caballoCO).join(torreCO)
dibfinal = Picture(fila1.img + fila2.img + filaVaciaBlanco.img + filaVaciaNegro.img + filaVaciaBlanco.img + filaVaciaNegro.img + fila7.img + fila8.img)

# Este draw une todas las filas creadas anteriormente y se genera el tablero completo
draw(dibfinal)