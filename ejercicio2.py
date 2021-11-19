#Millas a metros
#1
# a = input(" Para convertir de millas a km ingrese 1, de lo contrario 2: ")
# a==1:

#Metodo profe
print("Aplicativo de conversiones millas-kilometros:\n")
print (" "*12 + "1. mi a Km")
print (" "*12 + "2. km a mi")
a = float(input("Ingrese la opción que desea escoger: "))


if a == 1:
    print("1. mi a Km")
    l = float(input("Ingrese su medida en mi: "))
    print ("La medida en km es: ", l/1.6,"km")
elif a == 2:
     print("2. km a mi")
     w = float(input("Ingrese su medida en millas: "))
     print("La medida en mi es: ", w*1.6, "mi")