
class ball:
    def __init__(self, ballCircuference = 40, color = "orange", material = "plastic" ):
        self.__ballCircuference = ballCircuference
        self.color = color
        self.material = material
        


    def showballcolor(self):
        return print(self.color)        
        
    def changeBallcolor(self, novaCor):
        novaCor = input("qual cor vc quer mudar ? ")
        self.color = novaCor
        
        
        
bola = ball()
bola.changeBallcolor("oraneeee")
bola.showballcolor()
print(bola.material)

