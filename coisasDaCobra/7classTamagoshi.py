..............fazendo


class tmagoshi:

    def __init__(self, name, hunger, HP, age ):
        self. name= name
        self. hunger= hunger
        self. HP= HP
        self. age= age
        
        


     
        
    def ChangeChanel(self, imput):

        if imput >= 1 :
            print("oooi")       
        else:
            print("canal invalido")
        
    def changeEveryThing (self):
        self.name = int(input("para qual nome vc gostaria de mudar ?"))
        # self.hunger = input("qual nivel de fome (1 a 100) ?")
        # self.HP= input("como esta a saude dele (1 a 100) ?")
        # self.age = input("quantos anos ele tem agr  ?")
        
        self.ChangeChanel(self.name)
        

xxx= tmagoshi("robeto", 60, 100, 20)


xxx.changeEveryThing()





