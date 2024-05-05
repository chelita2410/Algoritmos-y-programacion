años_bisiestos = []
seguir = True
while seguir:
    nuevoAño = int(input("ingrese un año: "))
    if nuevoAño <= 1900:
        print("tu año tiene que ser mayor a 1900")
        continue
    elif nuevoAño >= 2199:
        print("tu año tiene que ser menor a 2199")
        continue 
    años_bisiestos.append(nuevoAño)
    break 
while True:
    if nuevoAño %4 != 0:
        print ("este año no es bisiesto")
        break
    elif nuevoAño %100 == 0 and año %400 != 0:
        print("este año no es bisiesto")
        break
    else:
        print("este año es bisiesto!")
        break

    