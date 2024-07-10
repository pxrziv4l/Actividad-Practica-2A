#ejercicio 4
print("\nPor favor ingrese su edad para el ejercicio.\n")
edad_usuario = int(input("Ingrese su Edad:"))
print("\nLa edad ingresada es",edad_usuario,"años.\n")
confirmar = input("¿Es correcto? ->")
if confirmar == "si" or "Si" or "SI":
    if edad_usuario > int(12) and edad_usuario < int(18):
        print("\nUsted es un adolescente.\n")
    else:
        print("\nNo es un adolescente.\n")     
else:
    print("\nLa edad no fue confirmada. Intentelo otra vez.\n")

#ejercicio 5
print("\nPor favor ingrese su edad para el ejercicio.\n")
edad_usuario = int(input("Ingrese su Edad: "))
print("\nLa edad ingresada es",edad_usuario,"años.\n")
confirmar = input("Confirma: ")
if confirmar == "si" or "Si" or "SI":
    if edad_usuario < int(10):
        print("\nUsted es un niño/a.\n")
    elif edad_usuario < int(13):
        print("\nUsted es un pre-adolescente.\n")
    elif edad_usuario < int(17):
        print("\nUsted es un adolescente.\n")    
else:
    print("\nLa edad no fue confirmada. Intentelo otra vez.\n")