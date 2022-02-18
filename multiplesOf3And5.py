#Crea la tabla. Funciona PERFECTO
def hacerTabla_aux(n, diferencia):
    grid = []

    # La mitad de la celda
    medio = n/2 + 1
    act = 1
    while act <= medio:
        grid.append(n-act-diferencia)
        act+=1
    # Ahora llego al medio
    act-=2
    while act >= 1:
        grid.append(n-act-diferencia)
        act-=1
    return grid

def hacerTabla(n):
    grid = []
    
    medio = n/2 + 1
    act = 0
    
    while act < medio-1:
        grid.append(hacerTabla_aux(n, act))
        act+=1
    act = n-1
    while act > medio:
        grid.append(hacerTabla_aux(n, act))
        act-=1

    return grid

def mover(posicion, direccion):
    pass

def sePuede(posicion, pasosAct):
    pass

def is_valid_walk(walk):
    grid = [
        [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10],
        [9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9],
        [8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8],
        [7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7],
        [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
        [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
        [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6],
        [7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7],
        [8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8],
        [9, 8, 7, 6, 5, 4, 5, 6, 7, 8, 9],
        [10, 9, 8, 7, 6, 5, 6, 7, 8, 9, 10]]

    # Ya tengo el grid hecho 11 x 11
    # Ahora necesito poner en cada celda los pasos necesarios para llegar al centro
    posicion = [5,5]
    pasosAct = 0
    valido = True
    while valido:
        #Si walk está vacia
        if len(walk) == 0:
            if posicion != [5,5]:
                valido = False
            else:

                break
        # Si ya no se puede llegar al centro
        elif pasosAct > 10 - grid[posicion[0]][posicion[1]]:
            valido = False
        # Caso crítico: se intenta acceder a una posicion que no existe
        else:
            actual = walk.pop(0)
            pasosAct += 1
            print(actual, pasosAct)
            if actual == "n":
                if sePuede(posicion, actual):
                    posicion[1] += 1
                else:
                    valido = False
            elif actual == "s":
                if sePuede(posicion,actual):
                    posicion[1] -= 1
                else:
                    valido = False
            if actual == "w":
                if sePuede(posicion, actual):
                    posicion[0] -= 1
                else:
                    valido = False
            elif actual == "e":
                if sePuede(posicion,actual):
                    posicion[0] += 1
                else:
                    valido = False

    return valido

if __name__ == "__main__":
    is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])



