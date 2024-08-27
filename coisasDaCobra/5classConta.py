class acount:
    def __init__(self, acountNumber, owner):
        self.money = 0
        self.__acountNumber = acountNumber
        self._owner=owner 


    def set_changeName (self):
        self._owner = input("para qual nome vc gostaria de mudar ?")
        

    def deposit(self, moneyIn):
       self.money += moneyIn 
       print(f"seu novo saldo é {self.money} ")

    def takeMoney(self, moneyOut):
        self.money -= moneyOut
        if self.money <= 0:
            print("seu saldo é negativo, não pode tirar esse valor ")
        else:
            print(f"seu novo saldo é {self.money}")



x = acount( 123, "roberto")
print("ola, ", x._owner)
x.deposit(2)
x.takeMoney(3)
x.set_changeName()
print("kkk")