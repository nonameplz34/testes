class square:
    def __init__(self, squareHeight = 40, testes = "olo" ):
        self.squareHeight = squareHeight
        self.__testes = testes



    def changeSidesHeight(self,):
        self.showSideHeight = int(input("qual é a nova altura?"))
        

    def showSideHeight(self):
        print(self.squareHeight)

    def areaOfSquare(self):
        print( self.squareHeight * 2)
       




x = square()
x.changeSidesHeight()
x.areaOfSquare()

