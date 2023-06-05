from dataclasses import replace
from email.mime import image
from mimetypes import init
from colors import *
from pieces import *
class Picture:
  def __init__(self, img):
    self.img = img
  
  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        aux = self.img[i][j] + aux
      image.append(aux)
      aux = ""
    
    return Picture(image)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      aux = self.img[len(self.img) - 1 - i] + aux
      image.append(aux)
      aux = ""
    
    return Picture(image)
  
  def negative(self):
    """ Devuelve un negativo de la imagen """
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        aux = aux + self._invColor(self.img[i][j])
      image.append(aux)
      aux = ""
    
    return Picture(image)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual """
    
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      aux = aux + self.img[i] + p.img[i]
      image.append(aux)
      aux = ""
    
    return Picture(image)

  def up(self, p):
    """Muetra self sofre otra p"""
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        if(self.img[i][j] != " "):
          aux = aux + self.img[i][j]
        else:
          aux = aux + p.img[i][j]
      image.append(aux)
      aux = ""
    
    return Picture(image)
  
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        if(p.img[i][j] != " "):
          aux = aux + p.img[i][j]
        else:
          aux = aux + self.img[i][j]
      image.append(aux)
      aux = ""
    
    return Picture(image)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n """
    
    aux = ""
    image = []
    
    for j in range(0, len(self.img)):
      for i in range(n):
        aux = aux + self.img[j]
      image.append(aux)
      aux = ""
    
    return Picture(image)

  def verticalRepeat(self, n):
    """Muestra self n veces hacia abajo"""
    
    image = []
    for i in range(n):
      image = image + self.img
  
    return Picture(image)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario o antihorario"""
    #return Picture(None)
