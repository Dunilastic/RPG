import random

class Personaje:
  def __init__(self, nombre, salud, magia, fuerza, fuerzaMagica, defensa, oro):
    self.nombre = nombre
    self.salud = salud
    self.magia = magia
    self.fuerza = fuerza
    self.fuerzaMagica = fuerzaMagica
    self.defensa = defensa
    self. oro = oro

  def ataque(self, enemigo):
    daño = max(0, random.randint(0, self.fuerza) - random.randint(0, enemigo.defensa))
    enemigo.salud -= daño
    return daño

  def curar(self):
    curacion = random.randint(0,self.magia)
    self.salud += curacion
    return curacion

  def estaVivo(self):
    return self.salud > 0
