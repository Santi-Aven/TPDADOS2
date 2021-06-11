# Cantidad de jugadores: 2
#
# Final del juego: Gana el jugador que alcance los x puntos o más, siendo x un valor que se ingresa por teclado (validar que x sea mayor a 10).
#
# Desarrollo del juego:
#
# A pedido del público, sólo se implementa la segunda ronda de las reglas enunciadas en el TP1 anterior.
# Es decir que, a su turno, cada jugador solo apuesta por par o impar. Si acierta gana el puntaje equivalente al dado de mayor valor,
# y adicionalmente este puntaje se duplica si todos los dados son de dicha paridad. Si pierde, resta el dado de menor valor (puede quedar con puntaje negativo).
#
# Se debe mostrar por cada turno el valor de los dados y el puntaje parcial del jugador.
#
# Al terminar el turno de ambos jugadores, se verifica si alguno de ellos alcanzó el puntaje objetivo. Si no es así,
# vuelven a jugar ambos (cada uno debe completar su turno) hasta finalizar el juego.
#
# Al terminar el juego, se debe mostrar el nombre y puntaje total obtenido de cada jugador e informar el nombre del ganador.
# Si ambos jugadores llegaran a tener el mismo puntaje final, gana aquel jugador que tenga la mayor cantidad de jugadas ganadas.
# Si coinciden también en cantidad de jugadas, entonces es un empate.
#
# Por último, se pide elaborar y mostrar las siguientes estadísticas:
#
# La cantidad de jugadas realizadas (recordando que una jugada consiste en los turnos de ambos jugadores).
# Si hubo al menos una jugada con puntaje empatado entre ambos jugadores.
# El puntaje promedio obtenido por jugada por cada jugador.
# El porcentaje de aciertos para cada jugador (considerando acierto si la suma de los dados coincidió con la paridad apostada).
# Indicar también si el ganador es el que tuvo mayor porcentaje de aciertos.
# Si algún jugador ganó en al menos 3 turnos seguidos.

# Reglas de la Segunda Ronda hola como estas yo estoy 
#
# a.) El primer jugador vuelve a lanzar los 3 dados, y se considera que apuesta tod0 el puntaje de la ronda anterior a par/impar
# (el programa debe pedir que el jugador elija si apuesta por par o impar).
#
# b.) Si la suma de los tres dados en esta segunda jugada es de la paridad elegida, entonces suma el dado de mayor valor a su puntaje de la ronda anterior;
# en caso contrario, resta el dado de menor valor a su puntaje anterior.
#
# c.) Si efectivamente la suma en la segunda jugada es de la paridad elegida, entonces el programa debe controlar
# si además los tres dados fueron de la paridad elegida, y en ese caso, se duplica el puntaje total.
#
# Se repite la jugada para el segundo jugador con las mismas reglas que el primero.

__author__ = "Grupo 177"

from soporte import *
import random


# Definimos la función "MENU"
def menu():
    print("------------")
    print("-TP DADOS 2-")
    print("1) Juego")
    print("2) ")
    print("3) Terminar programa ")
    print("------------")
    op = int(input("\033[1;32m" + "Ingrese una opción: \033[0m"))
    return op


def valor_x():
    x = 0
    while x <= 10:
        x = int(input("¿A qué valor hay que llegar? (Mayor de 10)  X: "))
        if x > 10:
            valor_correcto()
        else:
            print("\033[31m" + "Opción incorrecta\033[0m")
            print("\033[31m" + "Ingresar número mayor a 10\033[0m")
        return x


# Definimos la función "MAIN", vendria a ser principal
def main():
    opcion = -1
    while opcion != 3:
        opcion = menu()
        if opcion == 1:
            valor_correcto()
            jugador1 = input("Ingrese el nombre del jugador 1: ")
            jugador2 = input("Ingrese el nombre del jugador 2: ")
            valor_x()

            # Turno jugador 1
            paridad = 0
            print("Va a apostar al impar(1) o al par(2)?")
            while paridad != 1 and paridad != 2:
                paridad = int(input("Paridad :"))





        elif opcion == 2:
            print("opcion 2")
        elif opcion == 3:
            print("Adios!")
        elif opcion < 1 or opcion > 3:
            print("\033[31m" + "Opción incorrecta\033[0m")


# script principal
if __name__ == "__main__":
    main()
