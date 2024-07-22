temperatura =float (input("Ingrese la temperatura a convertir:"))
TipoTem = input("Es Farhenheit(F) o Celsius(C)?:")
if TipoTem == "C" or "c":
    F = ((temperatura * 1.8) + 32)
    print("La temperatura en Farhenheit es:", F)
elif TipoTem == "F" or "f":
    C = ((temperatura - 32)/1.8)
    print("La temperatura en Celsius es:", C)
else:
    print("La escala ingresada no es valida")