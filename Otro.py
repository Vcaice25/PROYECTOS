from abc import ABC, abstractmethod

class Cuenta(ABC):
    def __init__(self, numero, nombre_propietario, saldo):
        self.numero = numero
        self.nombre_propietario = nombre_propietario
        self.saldo = saldo

    @abstractmethod
    def credito(self, valor):
        pass

    @abstractmethod
    def debito(self, valor):
        pass

    @abstractmethod
    def mostrar_saldo(self):
        pass


class CuentaAhorro(Cuenta):
    def __init__(self, numero, nombre_propietario, saldo, interes):
        super().__init__(numero, nombre_propietario, saldo)
        self.interes = interes

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print("No se puede realizar la operación. Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def pagar_interes(self):
        interes_generado = self.saldo * self.interes
        self.saldo += interes_generado


class CuentaCorriente(Cuenta):
    def __init__(self, numero, nombre_propietario, saldo, tiene_chequera):
        super().__init__(numero, nombre_propietario, saldo)
        self.tiene_chequera = tiene_chequera

    def credito(self, valor):
        self.saldo += valor

    def debito(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print("No se puede realizar la operación. Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

    def pagar_cheque(self, valor):
        if self.tiene_chequera:
            if self.saldo - valor >= 0:
                self.saldo -= valor
            else:
                print("No se puede realizar la operación. Saldo insuficiente.")
        else:
            print("No se puede pagar el cheque. La cuenta no tiene chequera.")


# Solicitar datos para la simulación de transacción

numero_cuenta = input("Ingrese el número de cuenta: ")
nombre_propietario = input("Ingrese el nombre del propietario de la cuenta: ")
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))

cuenta_ahorro = CuentaAhorro(numero_cuenta, nombre_propietario, saldo_inicial, 0.05)

print("=== Cuenta de Ahorro ===")
cuenta_ahorro.mostrar_saldo()

monto_credito = float(input("Ingrese el monto a depositar: "))
cuenta_ahorro.credito(monto_credito)

monto_debito = float(input("Ingrese el monto a retirar: "))
cuenta_ahorro.debito(monto_debito)

cuenta_ahorro.pagar_interes()

print("=== Cuenta de Ahorro ===")
cuenta_ahorro.mostrar_saldo()


numero_cuenta = input("Ingrese el número de cuenta: ")
nombre_propietario = input("Ingrese el nombre del propietario de la cuenta: ")
saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
tiene_chequera = input("¿La cuenta tiene chequera? (S/N): ").upper() == "S"

cuenta_corriente = CuentaCorriente(numero_cuenta, nombre_propietario, saldo_inicial, tiene_chequera)

print("=== Cuenta Corriente ===")
cuenta_corriente.mostrar_saldo()

monto_credito = float(input("Ingrese el monto a depositar: "))
cuenta_corriente.credito(monto_credito)

monto_debito = float(input("Ingrese el monto a retirar: "))
cuenta_corriente.debito(monto_debito)

if tiene_chequera:
    monto_cheque = float(input("Ingrese el monto del cheque a pagar: "))
    cuenta_corriente.pagar_cheque(monto_cheque)

print("=== Cuenta Corriente ===")
cuenta_corriente.mostrar_saldo()
