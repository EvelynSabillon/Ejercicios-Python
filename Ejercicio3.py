
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print('No se puede retirar la cantidad: '+str(cantidad)+' porque es mayor al saldo')
        else:
            self.saldo -= cantidad
            return self.saldo

    def mostrar_saldo(self):
        print(f'Su saldo es de: {self.saldo}')


cuenta1 = CuentaBancaria("Pancho Pistolas")
cuenta1.depositar(1000)
cuenta1.mostrar_saldo()
cuenta1.retirar(500)
cuenta1.mostrar_saldo()
cuenta1.retirar(600)
cuenta1.mostrar_saldo()
cuenta1.retirar(100)
cuenta1.mostrar_saldo()
cuenta1.depositar(10000)
cuenta1.mostrar_saldo()