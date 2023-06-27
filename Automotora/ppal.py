import funciones as fn
propietarios=[]
ruts=[]
fonos=[]
correos=[]
patentes=[]
annios=[]
combustibles=[]
puertas=[]
transmisiones=[]
colores=[]
kilometrajes=[]
precios=[]
opc=0
while opc != 5:
    opc=fn.menu()
    if opc==1:
        propietarios,ruts,fonos,correos,patentes,combustibles,puertas,transmisiones,colores,kilometrajes,annios,precios=fn.agregarAuto(propietarios,
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
        precios)
    elif opc==2:
        fn.mostrarAuto(propietarios,annios,patentes,combustibles,puertas,kilometrajes, precios)
    elif opc==3:
        patentes, precios, kilometrajes=fn.modificaAuto(patentes, precios, kilometrajes)
    elif opc==4:
       propietarios,ruts,fonos,correos,patentes,combustibles,puertas,transmisiones,colores,kilometrajes,annios,precios=fn.venderAuto(propietarios,
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
        precios) 


