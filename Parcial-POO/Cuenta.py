from datetime import datetime
import random

class Cuenta:

    numero_de_cuentas = 0

    def __init__(self, titular, fecha_apertura, n_cuenta, saldo):
        self.__ID = Cuenta.numero_de_cuentas
        self.titular = titular
        self.fecha_apertura = fecha_apertura
        self.n_cuenta = n_cuenta
        self.__saldo = saldo
        Cuenta.numero_de_cuentas += 1

    def get_saldo(self):
        return self.__saldo

    def ingresar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if self.__saldo > cantidad:
            self.__saldo -= cantidad
        else: cantidad = 0
        return cantidad

    def transferir(self, cuenta_dest, cantidad, com):
        if self.__saldo > (1+(com/100))*cantidad:
            self.__saldo -= (1+(com/100))*cantidad
            cuenta_dest.__saldo += cantidad
        else:
            cantidad = 0
        return cantidad


class Plazo_fijo(Cuenta):

    def __init__(self, titular, fecha_apertura, n_cuenta, saldo, fecha_vencimiento):
        super().__init__(titular, fecha_apertura, n_cuenta, saldo)
        self.fecha_vencimiento = fecha_vencimiento

        def retirar(self, cantidad):
            if fecha_vencimiento >= datetime.datetime.now():
                super().retirar(1.05*cantidad)

            else: super().retirar(cantidad)

        def transferencia(self, cuenta_dest, cantidad):
            if fecha_vencimiento >= datetime.datetime.now():
                super().transferir(cuenta_dest, cantidad, 5)

            else:
                super().transferir(cuenta_dest, cantidad, 0)


class Vip(Cuenta):

    def __init__(self, titular, fecha_apertura, n_cuenta, saldo, saldo_neg_max):
        super().__init__(titular, fecha_apertura, n_cuenta, saldo + saldo_neg_max)
        self.saldo_neg_max = saldo_neg_max

    def get_saldo(self):
        return super().get_saldo() - self.saldo_neg_max


def main():

    cuenta1 = Cuenta("Pepe", datetime(2022,4,1)+(datetime(2024,5,25)-datetime(2022,4,1))*random.random(), random.randint(100000000000,1000000000000), 10000)

    cuenta2 = Plazo_fijo("Mariaflores", datetime(2022,4,1)+(datetime(2024,5,25)-datetime(2022,4,1))*random.random(), random.randint(100000000000,1000000000000), 10000, datetime(2024,4,1)+(datetime(2026,5,25)-datetime(2024,4,1))*random.random())

    cuenta3 = Vip("Juanito", datetime(2022,4,1)+(datetime(2024,5,25)-datetime(2022,4,1))*random.random(), random.randint(100000000000,1000000000000), 10000, 1000)

    cuenta1.transferir(cuenta3,2000, 0)

    cuenta3.ingresar(575)

    cuenta2.retirar(780)

    print(str(cuenta1.get_saldo()) + " " + str(cuenta2.get_saldo()) + " " + str(cuenta3.get_saldo()))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
