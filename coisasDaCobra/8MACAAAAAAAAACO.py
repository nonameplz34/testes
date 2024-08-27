...........fazendo 

class monkey :
    def __init__(self, name, ) :
        self.name = name
        self.bucho= ["banana", "maça", "bronzePipe"]
        

    def eat (self):
        food = input("qual comida ele vai comer?")
        self.bucho.append(food)

    def digest (self):
        self.bucho.pop(0)

    def seeBucho (self):
        print(self.bucho)
    
    def feeding (self):
        timesFeeding = int(input(f"quantas vezes vai alimentar o {self.name}?"))
        # int(input("quantas vezes vai alimentar o ", self.name, "?"))
        for i in range(timesFeeding):
         self.eat()
            
        


MACACO1 = monkey("muufaza")
MACACO2 = monkey("simba")

MACACO1.feeding()
