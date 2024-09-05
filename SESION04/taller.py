'''
Crear un programa en python que permita crear objetos de la clase CuentaBancaria, cuyos atributos son: numeroCta, nombreCliente, saldoCta, fechaApertura, ultimoRetiro, ultimaConsignacion.
Tambien crear objetos de la clase cuenta ahorros, cuyos atributos son: cdt, sinCobro.
Tambien crear objetos de la clase cuenta corriente, cuyos atributos son: cheques, impuestos .
Aplicar encapsulamiento y definir los métodos apropiados para controlar y gestionar los atributos de los objetos creados.
Utilizar un menu para las diferentes opciones, tales como crearCta, aperturaCta, consignar, retirar y transferencia entre otros.
Y que en crear cuenta, genere que tipo de cuenta si de ahorros o corriente
'''

class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura):
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = None
        self.__ultimaConsignacion = None

    def consignar(self, monto):
        self.__saldoCta += monto
        self.__ultimaConsignacion = monto

    def retirar(self, monto):
        if monto <= self.__saldoCta:
            self.__saldoCta -= monto
            self.__ultimoRetiro = monto
        else:
            print("Saldo insuficiente")

    def mostrar_informacion(self):
        print(f"Cuenta: {self.__numeroCta}, Cliente: {self.__nombreCliente}, Saldo: {self.__saldoCta}")

    def transferir(self, monto, cuenta_destino):
        if monto <= self.__saldoCta:
            self.retirar(monto)
            cuenta_destino.consignar(monto)
            print(f"Transferencia de {monto} realizada a la cuenta {cuenta_destino.__numeroCta}")
        else:
            print("Saldo insuficiente para la transferencia")

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura, cdt, sinCobro):
        super().__init__(numeroCta, nombreCliente, saldoCta, fechaApertura)
        self.__cdt = cdt
        self.__sinCobro = sinCobro

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numeroCta, nombreCliente, saldoCta, fechaApertura, cheques, impuestos):
        super().__init__(numeroCta, nombreCliente, saldoCta, fechaApertura)
        self.__cheques = cheques
        self.__impuestos = impuestos

def buscar_cuenta(numeroCta, cuentas):
    for cuenta in cuentas:
        if cuenta._CuentaBancaria__numeroCta == numeroCta:
            return cuenta
    return None

def menu():
    cuentas = []
    while True:
        print("\n--- Menú ---")
        print("1. Crear cuenta")
        print("2. Apertura cuenta")
        print("3. Consignar")
        print("4. Retirar")
        print("5. Transferencia")
        print("6. Mostrar información")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de cuenta (ahorros/corriente): ")
            numeroCta = input("Número de cuenta: ")
            nombreCliente = input("Nombre del cliente: ")
            saldoCta = float(input("Saldo inicial: "))
            fechaApertura = input("Fecha de apertura: ")

            if tipo == "ahorros":
                cdt = input("CDT: ")
                sinCobro = input("Sin cobro (sí/no): ")
                cuenta = CuentaAhorros(numeroCta, nombreCliente, saldoCta, fechaApertura, cdt, sinCobro)
            elif tipo == "corriente":
                cheques = input("Cheques: ")
                impuestos = input("Impuestos: ")
                cuenta = CuentaCorriente(numeroCta, nombreCliente, saldoCta, fechaApertura, cheques, impuestos)
            else:
                print("Tipo de cuenta no válido")
                continue

            cuentas.append(cuenta)
            print("Cuenta creada exitosamente")

        elif opcion == "2":
            numeroCta = input("Número de cuenta: ")
            cuenta = buscar_cuenta(numeroCta, cuentas)
            if cuenta:
                print("Cuenta encontrada:")
                cuenta.mostrar_informacion()
            else:
                print("Cuenta no encontrada")

        elif opcion == "3":
            numeroCta = input("Número de cuenta: ")
            cuenta = buscar_cuenta(numeroCta, cuentas)
            if cuenta:
                monto = float(input("Monto a consignar: "))
                cuenta.consignar(monto)
                print("Consignación realizada")
            else:
                print("Cuenta no encontrada")

        elif opcion == "4":
            numeroCta = input("Número de cuenta: ")
            cuenta = buscar_cuenta(numeroCta, cuentas)
            if cuenta:
                monto = float(input("Monto a retirar: "))
                cuenta.retirar(monto)
                print("Retiro realizado")
            else:
                print("Cuenta no encontrada")

        elif opcion == "5":
            numeroCta_origen = input("Número de cuenta origen: ")
            cuenta_origen = buscar_cuenta(numeroCta_origen, cuentas)
            if cuenta_origen:
                numeroCta_destino = input("Número de cuenta destino: ")
                cuenta_destino = buscar_cuenta(numeroCta_destino, cuentas)
                if cuenta_destino:
                    monto = float(input("Monto a transferir: "))
                    cuenta_origen.transferir(monto, cuenta_destino)
                else:
                    print("Cuenta destino no encontrada")
            else:
                print("Cuenta origen no encontrada")

        elif opcion == "6":
            for cuenta in cuentas:
                cuenta.mostrar_informacion()

        elif opcion == "7":
            break

        else:
            print("Opción no válida")

menu()
