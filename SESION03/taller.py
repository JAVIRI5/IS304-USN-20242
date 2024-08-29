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

'''
("Presione 1 para ver el numero de Cuenta")
("Presione 2 para atender a la persona al frente de la fila")
("Presione 3 para mostrar el estado de la fila")
("Presione 4 para finalizar")
("Presione 5 para finalizar")
("Presione 6 para finalizar")
("Presione 7 para finalizar")
'''
            
class CuentaBancaria:
    
    def __init__(self,numeroCta,nombreCliente,saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion):
        
        set(numeroCta,nombreCliente,saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion)
    
    def set (self,numeroCta,nombreCliente,saldoCta,fechaApertura,ultimoRetiro,ultimaConsignacion):
        
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__saldoCta = saldoCta
        self.__fechaApertura = fechaApertura
        self.__ultimoRetiro = ultimoRetiro
        self.__ultimaConsignacion = ultimaConsignacion
    
    def set_numeroCta(self,x):
        self.__numeroCta = x
    
    def set_nombreCliente(self,x):
        self.__nombreCliente = x
        
    def set_saldoCta(self,x):
        self.__saldoCta = x
        
    def set_fechaApertura(self,x):
        self.__fechaApertura = x
        
    def set_ultimoRetiro(self,x):
        self.__ultimoRetiro = x
        
    def set_ultimaConsignacion(self,x):
        self.__ultimaConsignacion = x
        
    
    def get_numeroCta(self,):
        return self.__numeroCta
    
    def get_nombreCliente(self,):
        return self.__nombreCliente
        
    def get_saldoCta(self,):
        return self.__saldoCta
        
    def get_fechaApertura(self,):
        return self.__fechaApertura
    
    def get_ultimoRetiro(self,):
        return self.__ultimoRetiro
        
    def get_ultimaConsignacion(self,):
        return self.__ultimaConsignacion
        
    
def main():

    p = CuentaBancaria(1,2,3,4,5,6)
    
    print(get_numeroCta())
