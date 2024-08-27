class rectangle:
    def __init__(self,  width = 6, heights = 9 ):
        self.width =  width
        self.heights = heights
        self.changeSide()


        
    def changeSide(self):
        choise = int(input("qual lado vc quer mudar? (1)altura (2)largura"))
        if choise == 1:  
            self.heights = int(input("a nova altura sera: "))
        else:
            self.width = int(input("a nova largura sera: "))
    
    def get_valeu(self):
        return print(f"Largura: {self.width}, Altura: {self.heights}")
    
    def area (self):
        print ( self.width * self.heights)
        
    def perimetro (self):
        print ( self.width * 2 + self.heights * 2)
        
 
        
x = rectangle()

x.get_valeu()
x.perimetro()
x.area()

print("help")
