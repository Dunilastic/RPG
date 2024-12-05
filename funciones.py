import random

def menu():
  print("¿Qué quieres hacer?")
  print("a. Atacar")
  print("b. Huir")
  opcion = input()
  return opcion

def combate(self, enemigo):
  if enemigo.estaVivo:
    daño = self.ataque(enemigo)
    print("Le has hecho "+str(daño)+" puntos de daño a "+enemigo.nombre)

def huir(jugador):
  print("")
  print("¡"+jugador.nombre+" intenta huir!")
  huir = random.randint(0, 10)
  if huir > 7:
    print("¡Has huido con éxito!")
    h = True
    return h
  else:
    print("¡No ha podido huir!")
    print("")

def lucha(jugador, enemigo):
  print("")
  print("¡"+jugador.nombre+" ataca!")
  if enemigo.estaVivo:
    daño = jugador.ataque(enemigo)
    print("Le has hecho "+str(daño)+" puntos de daño a "+enemigo.nombre)

  print(jugador.nombre+": "+str(jugador.salud)+"PS")
  print(enemigo.nombre+": "+str(enemigo.salud)+"PS")

  print("")
  print("¡"+enemigo.nombre+" ataca!")
  if enemigo.estaVivo:
    daño = enemigo.ataque(jugador)
    print("Le has hecho "+str(daño)+" puntos de daño a "+enemigo.nombre)

  print(jugador.nombre+": "+str(jugador.salud)+"PS")
  print(enemigo.nombre+": "+str(enemigo.salud)+"PS")
  input(print(" "))
