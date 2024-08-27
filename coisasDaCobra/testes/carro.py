from datetime import *
import random
class Carro:
    # Construtor :: quando inicializo o objeto será executado este passo
    def __init__(self, chassi, ano, modelo):
        # code
        self.chassi = chassi
        self.__ano = ano
        self.modelo = modelo
        self.__odo = 0
        self.__crlv = None
        self.__medidor_combustivel = 0

    # Metodo

    def km(self):
        return self.__odo

    def acelerar(self, push):
        self.__odo = self.__odo + 1 * push

    @property
    def crlv(self):
        return self.__crlv

    @crlv.setter
    def crlv(self, year):
        year = datetime.today().year
        self.__crlv = year

    @property
    def medidor(self):
        return self.__medidor_combustivel

    @medidor.setter
    def medidor(self, litros):
        self.__medidor_combustivel =  self.__medidor_combustivel + litros
        print("ooi")


c= Carro(5, 5, 5)


    # def set_ano(self, ano):
    #     self.__ano = ano
    #
    # def get_ano(self):
    #     return self.__ano

'''
qtd_carro = int(input("Digite a quantidade de carros na frota: "))
frota = [] # lista vazia

for i in range(qtd_carro):
    chassi = input("Digite o chassi: ")
    ano = datetime.today().year
    modelo = input("Digite o modelo: ")
    frota.append(Carro(chassi=chassi, ano=ano, modelo=modelo))


numero_bandeirada = int(input("Digite o número de partidas: "))

for i in range(numero_bandeirada):
    for carro in frota:
        push = random.randrange(1,10)
        carro.acelerar(push)

for carro in frota:
    print("Carro:", carro.modelo, " KM: ", carro.km())
'''



# creta = Carro("123456", 2024, "Creta")
# # corsa = Carro("01234",2024,"corsa")
#
# # print(creta.get_ano())
# # creta.set_ano(1900)
# # print(creta.get_ano())
#
# creta.crlv = "2000"
# print(creta.crlv)
