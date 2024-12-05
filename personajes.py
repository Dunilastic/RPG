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

def presentacion():
  print("Un cielo azúl radiante te acompaña el día de hoy, eres...")
  input(print(""))
  print("Un momento... ¿Quién eres?")
  nombre = input(print("Introduce tu nombre: ")
  print("¡Ah sí! "+nombre+", ¿cómo olvidarme de ti?")
  input(print("Pues ahí ibas tú, "+nombre+", paseando por el bosque, cuando de repente aparece ante ti un orco...")
  input(print("¡Y empieza el combate!"))
