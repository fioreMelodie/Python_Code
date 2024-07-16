# Ejercicio: Pedir los datos de un estudiante de sexto 
# para averiguar qué edad tendrá cuando esté en Decimo grado

edad =input ("Escriba su edad actual: ")
edadDec = (int(edad)) 
edad2 = (float(edad))
print(type(edadDec))
print(type(edad2))
print("Usted va a tener:",(edadDec + 3),"años en grado Decimo")
print("Edad en decimal:",(edad2 + 3),"años en grado Decimo")


#Ejercicio 2: Pedir información general al usuario para entrevista y mostrarla en un informe

Nombre  = input ("Ingrese primer y segundo nombre (Si cuenta con este):")
Apellido = input("Ingrese Primer y Segundo apellido:")
id = input("Ingrese su numero de documento:")
TipoDoc = input("Ingrese el tipo de documento:")
Nacimiento = input ("Ingrese fecha de nacimiento con el formato (dd/mm/aaaa):")
CiudadNa = input ("Ingrese su Ciudad de nacimiento:")
PaisNa = input("Ingrese Pais de Nacimiento:")
EdadAct = input("Ingrese su edad actual:")
NomEmpresa = input("Ingrese el nombre de la empresa a la cual pertenece:")
NomCargo = input("Ingrese el cargo al cual se está presentando:")
Interes = input("Escriba el porqué quiere estar en el cargo: (Estoy interesad@ en participar...)")

NomCargo2 =(NomCargo.upper())

print("Buen día señores",NomEmpresa,", mi nombre es", Nombre, Apellido,"nacid@ en la ciudad de", CiudadNa,
      "ubicada en", PaisNa, ", me identifico con",TipoDoc, id,", actualmente tengo",EdadAct,
      "años. El motivo por el cual escribo este informe es porque ví la vacante en el cargo", 
      NomCargo2,"y",Interes, "Muchas gracias por la atención")


