#definimos el método parqa clasificar por edades los grupos deportivos
def categoria_deportiva (edad):
    if edad >=6 and edad<=7:
        return ('Pertenece a la categoría benjamín')
    elif edad >=8 and edad<=9:
        return ('Pertenece a la categoría alevín')
    elif edad >=10 and edad<=11:
        return ('Pertenece a la categoría infantil')
    elif edad>12:
        return ('Pertenece a la categoría cadete')
    else:
        return ('No se puede clasificar la edad introducida')

#input para introducir la edad
edad=input('Introduzca una edad')
edad=int(edad)
categoria_deportiva(edad)