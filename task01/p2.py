def caracter(character):
    global simbolo
    simbolo = ""
    global Fin
    Fin = ""
    if(character == '0'):
        simbolo = "0"
        return 0, True
    else:
        if(character == '1'):
            simbolo = "1"
            return 1, True
        else:
            if(character == Fin):
                return 2, True
        print("ERROR:", character, "No es valido")
        return -1, False


def encabezado():
    print("|  Edo. Actual  |  Caracter  |  Simbolo  |  Edo. Siguiente  |")
    body()


def contenido(estadosig, character, simbolo, estado):
    print("|      q{}       |      {}     |     {}     |        q{}        |".format(
        estadosig, character, simbolo, estado))
    body()


def body():
    print("+---------------+------------+-----------+------------------+")


def messageSuccess():
    print("|                       Cadena Valida                       |")
    print("+-----------------------------------------------------------+")


def messageInvalid():
    print("|                     Cadena No Valida                      |")
    print("+-----------------------------------------------------------+")


def main():
    '''
    Tabla de transiciones del automata AFD creado
    E: Error, A: Aceptado
    '''
    tabla = [
        [0, 1, "A"],
        [1, 2, "A"],
        [2, 3, "A"],
        [3, 4, "A"],
        [4, 4, "E"]
    ]
    estado = 0
    valid = True

    print("+-------------------------------------+")
    print("|    Ingrese una cadena a evaluar:    |")
    print("+-------------------------------------+")

    cadena = input()
    body()
    encabezado()

    for character in cadena:
        estadosig = estado

        charcaracter, valid = caracter(character)
        estado = tabla[estado][charcaracter]

        if (estado == "E" or not valid):
            print("|      q{}       |      {}     |           |                  |".format(
                estadosig, character))
            body()
            messageInvalid()
            break
        contenido(estadosig, character, simbolo, estado)

    if valid:
        if (estado == 4):
            messageInvalid()
        else:
            print(
                "|      q{}       |            |    FND    |                  |".format(estado))
            body()
            messageSuccess()


if __name__ == '__main__':
    main()
