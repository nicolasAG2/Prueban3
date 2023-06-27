def menu():
    print("~"*50)
    print("\tAutomotora PGY1121")
    print("~"*50)
    print("1.- Agregar auto")
    print("2.- Mostrar auto")
    print("3.- Modificar auto")
    print("4.- Vender auto")
    print("5.- SALIR")
    return validaNro(int,"Opción --> ",1,5)

def validaNro(tipo, texto, rMin=None,rMax=None):
    while True:
        try:
            nro=tipo(input(texto))
            if rMin != None and rMax != None:
                if rMin<=nro<=rMax:
                    break
                else:
                    print("Fuera de rango!!")
            elif rMin != None:
                if rMin<=nro:
                    break
                else:
                    print(f"el valor mínimo puede ser {rMin}")
            elif rMax != None:
                if nro<=rMax:
                    break
                else:
                    print(f"el valor máximo puede ser {rMax}")
            else:
                break
        except:
            print("Se esperaba un número!!")
    return nro

def validaLen(texto, large, estricto):
    while True:
        entrada=input(texto)
        if estricto:
            if len(entrada)== large:
                break
            else:
                print(f"El largo debe ser igual a {large}")
        else:
            if len(entrada) >= large:
                break
            else:
                print(f"El largo mínimo es {large}")
    return entrada

def validaMail():
    while True:
        correo=validaLen("Ingrese su email => ",6, False)
        if '@' in correo:
            if '.' in correo:
                break
            else:
                print("Falta el punto (.) dentro del correo")
        else:
            print("Falta el (@) dentro el correo.")
    return correo    

def validaPatentes(patentes):
    while True:
        patente=validaLen("Ingrese patente => ", 6, True)
        if len(patentes) != 0:
            existe=False
            if patente in patentes:
                existe=True
            if existe:
                print("Pantente YA Existe!!")
            else:
                break
        else:
            break
    return patente

def agregarAuto(propietarios,
                ruts,
                fonos,
                correos,
                patentes,
                combustibles,
                puertas,
                transmisiones,
                colores,
                kilometrajes,
                annios,
                precios):
    #valido (si corresponde) antes de agregar a las listas
    propietarios.append(input("Ingrese nombre => "))
    #Rut debe ser como mínimo 5000000 y no más de 99000000
    ruts.append(validaNro(int,"Ingrese RUT => ", 5000000,99000000))
    #El teléfono debe tener 9 dígitos
    fonos.append(validaLen("Ingrese su fono => ", 9, True))
    #Correo debe tener ‘@’, ‘.’ y como mínimo 6 dígitos
    correos.append(validaMail())
    #La patente debe tener 6 dígitos y debe ser única.
    patentes.append(validaPatentes(patentes))
    #Combustible solo puede ser ‘Diesel’ o ‘Kerosene’
    combustible = validaNro(int, "Ingrese combustible [1: Diesel / 2: Kerosene] =>",1,2)
    if combustible==1:
        combustibles.append("DIESEL")
    else:
        combustibles.append("KEROSENE")
    #Cantidad de puertas debe ser como mínimo 2
    puertas.append(validaNro(int,"Ingrese cantidad de puertas",2))
    # Tipo de Transmisión ‘M’ o ‘A’
    while True:
        transmision=input("Ingrese Transmisión [A: Automático / M: Mecánico] => ").upper()
        if transmision=='A' or transmision=='M':
            transmisiones.append(transmision)
            break
        else:
            print("Transmisión Incorrecta!!")
    colores.append(input("Ingrese color del auto => "))
    kilometrajes.append(validaNro(int,"Ingrese kilometraje => ", 0))
    annios.append(validaNro(int,"Ingrese año del vehículo => ",1990))
    precios.append(validaNro(int,"Ingrese valor de venta => $", 500000))
    print("Vehículo ingresado con Exito!!!")
    return propietarios,ruts,fonos,correos,patentes,combustibles,puertas,transmisiones,colores,kilometrajes,annios,precios

def mostrarAuto(propietarios,annios,patentes,combustibles, puertas, kilometrajes, precios):
    if len(patentes) != 0: 
        opc=validaNro(int,"1.- Por año\n2.-Por Km\n3.-Por $$ \n=>",1,3)
        print("Listado de Autos")
        print("~"*50)
        if opc==1:
            annio=validaNro(int,"Ingrese año => ", 1990)
            for a in range(len(propietarios)):
                if annio <= annios[a]:
                    print(f"{patentes[a]} | {combustibles[a]} | {propietarios[a]} | {puertas[a]} | {kilometrajes[a]} | {precios[a]}")
        elif opc==2:
            km=validaNro(int,"Ingrese km => ", 0)
            for a in range(len(propietarios)):
                if km <= kilometrajes[a]:
                    print(f"{patentes[a]} | {combustibles[a]} | {propietarios[a]} | {puertas[a]} | {kilometrajes[a]} | {precios[a]}")
        elif opc==3:
            precio=validaNro(int,"Ingrese $ => ", 500000)
            for a in range(len(propietarios)):
                if precio <= precios[a]:
                    print(f"{patentes[a]} | {combustibles[a]} | {propietarios[a]} | {puertas[a]} | {kilometrajes[a]} | {precios[a]}")
    else:
        print("Aún no hay vehiculos!!")

def buscaPatente(patentes):
    while True:
        patente=validaLen("Ingrese patente => ",6, True)
        existe=False
        for p in range(len(patentes)):
            if patente== patentes[p]:
                existe=True
                return p
        if not existe:
            return -1

def modificaAuto(patentes, precios, kilometrajes):
    if len(patentes) !=0:
        opc=validaNro(int,"1.- Modifica Precio\n2.-Modifica Km \n=>",1,2)
        pos=buscaPatente(patentes)
        if pos != -1:
            if opc==1:
                newPrecio=validaNro(int,"Ingrese nuevo precio => $", 500000)
                precios[pos]=newPrecio
            else:
                newKm=validaNro(int,"Ingrese nuevo km => ", 0)
                kilometrajes[pos]=newKm
            print("Modificado con Exito!!")
        else:
            print("La patente NO existe!!!")
    else:
        print("Aún no hay vehiculos!!")
    return patentes, precios, kilometrajes

def venderAuto(propietarios,
                ruts,
                fonos,
                correos,
                patentes,
                combustibles,
                puertas,
                transmisiones,
                colores,
                kilometrajes,
                annios,
                precios):
    if(len(patentes)!=0):
        p = buscaPatente(patentes)
        if p != -1:
            propietarios.pop(p)
            ruts.pop(p)
            fonos.pop(p)
            correos.pop(p)
            patentes.pop(p)
            annios.pop(p)
            combustibles.pop(p)
            puertas.pop(p)
            transmisiones.pop(p)
            colores.pop(p)
            kilometrajes.pop(p)
            precios.pop(p) 
            print("Vendido con EXITO!!!")
        else:
            print("Patente No Existe!!")
    else:
        print("No hay vehículos registrados!!")
    return propietarios,ruts,fonos,correos,patentes,combustibles,puertas,transmisiones,colores,kilometrajes,annios,precios
