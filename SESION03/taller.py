'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''
'''
Edicson Javier Rico Peralta
Unimonserrate
Jornada Nocturna
Estructura de datos
'''

'''
Crear un programa que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como aperturaCta, consignar, retirar y transferencia entre otros.
'''

class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = 0
        self.__ultimaConsignacion = 0

    def consignar(self, monto):
        if monto > 0:
            self.__saldoCta += monto
            self.__ultimaConsignacion = monto
            print(f"Se ha consignado {monto} en la cuenta.")
        else:
            print("El monto de consignación debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldoCta:
            self.__saldoCta -= monto
            self.__ultimoRetiro = monto
            print(f"Se ha retirado {monto} de la cuenta.")
        else:
            print("Saldo insuficiente o monto inválido para retiro.")

    def mostrar_detalles(self):
        print(f"Cliente: {self.__nombreCliente}")
        print(f"Número de cuenta: {self.__numeroCta}")
        print(f"Saldo actual: {self.__saldoCta}")
        print(f"Fecha de apertura: {self.__fechaApertura}")
        print(f"Último retiro: {self.__ultimoRetiro}")
        print(f"Última consignación: {self.__ultimaConsignacion}")

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Mostrar detalles de la cuenta")
    print("2. Consignar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

# Crear una instancia de CuentaBancaria
cuenta = CuentaBancaria(12345, "Juan Pérez", 1000.0, "01/01/2023")

# Mostrar opciones del menú
while True:
    mostrar_menu()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        cuenta.mostrar_detalles()
    elif opcion == "2":
        monto = float(input("Ingrese el monto a consignar: "))
        cuenta.consignar(monto)
    elif opcion == "3":
        monto = float(input("Ingrese el monto a retirar: "))
        cuenta.retirar(monto)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
