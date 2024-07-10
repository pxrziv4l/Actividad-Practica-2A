#ejercicio 5
print("\nPor favor ingrese su edad para el ejercicio.\n")
edad_usuario = int(input("Ingrese su Edad: "))
print("\nLa edad ingresada es",edad_usuario,"años.")
confirmar = input("Confirma: ")
if confirmar == "si" or confirmar == "Si" or confirmar == "SI":
    if edad_usuario < int(10):
        print("\nUsted es un niño/a.\n")
    elif edad_usuario < int(13):
        print("\nUsted es un pre-adolescente.\n")
    elif edad_usuario <= int(17):
        print("\nUsted es un adolescente.\n")    
else:
    print("\nLa edad no fue confirmada. Intentelo otra vez.\n")