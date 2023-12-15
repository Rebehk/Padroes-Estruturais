from abc import ABC, abstractclassmethod

class Dispositivo(ABC):
    @abstractclassmethod
    def ligar(self):
        pass

    @abstractclassmethod
    def desligar(self):
        pass


class TV(Dispositivo):
    def ligar(self):
        print("TV ligada")

    def desligar(self):
        print("TV desligada")


class Radio(Dispositivo):
    def ligar(self):
        print("Rádio ligado")

    def desligar(self):
        print("Rádio desligado")


class ControleRemoto:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def ligar(self):
        self.dispositivo.ligar()

    def desligar(self):
        self.dispositivo.desligar()


if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    controle_tv = ControleRemoto(tv)
    controle_radio = ControleRemoto(radio)

    controle_tv.ligar()
    controle_tv.desligar()

    controle_radio.ligar()
    controle_radio.desligar()
