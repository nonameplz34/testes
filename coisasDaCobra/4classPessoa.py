#corrigir depois, 


import random
class pepleo:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.weight = weight
        self.age = age
        self.height= height 
        
    def aging (self, yearspassed):
        # não ira funcinar se for chamado mais de uma vez, colocar yearsPass nas condiçoes e soma-lo no final do if
        
        self.age += yearspassed
        
        if self.age >= 100:
            print("foi mal vc morreu :( ")  
            
            #descobri quando estava fazendo a diferença 
            #não corrigi para não perder muito tempo em 1 unico exercicio 
            #estou levando em consideração q so vai executar 
        elif self.age >=21:
            print("ja não vai crescer mais que isso 😂")
            
            self.height += 21 * 5 / 100
            
            print(f" agr vc tem, ", self.age, " anos. " , self.height,"de altura e ganhou ", random.randint(1, 10),"kg")
        else:
            self.height += yearspassed * 5 / 100
            print(f" agr vc tem,", self.age, "anos. " , self.height,"de altura e ganhou ", random.randint(1, 10),"kg")
            
    def gaiWeight (self):
        
        random.randint(1, 10)
    def loseWeight (self):
        random.randint(1, 10)
    def grow(self):
        random.randint(1, 10)
        
bobo = 1
asd=pepleo("dom", 0, 0, 1)

asd.aging(50)
bobo=2
