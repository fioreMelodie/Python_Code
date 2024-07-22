puntaje = 45
if puntaje >= 95:    #El "if" es un condicional que permite afirmar si una conidición es afirmativa o no
    print("Aprobado con honores")
elif puntaje >= 50:  #Cuando la condición del "if" no se cumple, se pasa la siguiente condición "elif"
    print("Alumno aprobado")
else:
    print("Reprobado")
     #Si tanto "if" como "elif" resultan ser "false" se pasa a un "else" que es la 
     #última parte del condicional si ninguna de las dos condiciones de arriba no se cumplen
print ("Proceso de puntaje finalizado")

# A TENER EN CUENTA: Las condiciones se ejecutan de arriba hacia abajo, lo que quiere decir que si por 
#por ejemplo en la condición asignada a "if" se cumple, no se validan las otras dos condiciones porque
#una ya dio como resultado "True"