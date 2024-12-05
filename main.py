import funciones
from personajes import Personaje


jugador = Personaje("Duni", 100, 50, 70, 50, 20, 99)
enemigo = Personaje("Orco", 80, 0, 30, 0, 10, 10)

print ("¡"+jugador.nombre+" se ha encontrado un enemigo!")
input(print(" "))
print ("¡Resulta que es un "+enemigo.nombre+"!")
input(print(" "))
print("¡Comienza el combate!")
print(jugador.nombre+" VS "+enemigo.nombre)
print(jugador.nombre+": "+str(jugador.salud)+"PS")
print(enemigo.nombre+": "+str(enemigo.salud)+"PS")
input(print(" "))

while jugador.salud > 0 and enemigo.salud > 0:
  opcion = funciones.menu()

  if opcion == "a":
    funciones.lucha(jugador, enemigo)

  else:
    h = funciones.huir(jugador)
    if h == True:
      break

if jugador.salud <= 0:
  print("Has perdido...")
elif enemigo.salud <=0:
  print("¡Has ganado!")

print("¡Hasta la siguiente aventura!")
