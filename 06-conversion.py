resultado =input("Ingresa tu edad: ") #Permite obtener datos del usuario (llamarlos)   
#y el resultado se registra en la variable

print(type(resultado)) #Permite ver el tipo de dato
numero = int(resultado) #Permite cambiar tipos de datos

#Ejemplo
str(22) #Pasa a tipo string
float("22.13") #Permite pasar a decimal
bool("un string") # Permite pasar a Booleano (True or False) pero con condiciones como
# Toma como "True" cualquier condición a excepción de los siguientes casos:
# (False), ("") string vacío, (0) el cero y el objeto (None)
print(2 + numero)