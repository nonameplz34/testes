class tv:

    def __init__(self, VolumeLevel ):
        self.curretChannel = range(30*2)

        self.VolumeLevel= VolumeLevel
    def TurnVolumeDown(self, number):        

        if self.VolumeLevel - number <= 0 :

            print("ja esta no zero, vai masi pra baixo não moço")

            self.VolumeLevel = 0

        else : 

            self.VolumeLevel -= number

            print("volume atual", self.VolumeLevel)   

    def TurnVolumeUp(self, number):

        if self.VolumeLevel + number < self.VolumeLevel:

            print("ai tu ta diminuindo parceiro")
            

        else:

            self.VolumeLevel += number

            print("volume atual", self.VolumeLevel)
        

    def ChangeChanel(self, nextChannel):

        if nextChannel in self.curretChannel :
            self.curretChannel = nextChannel
            print("canal atual:", nextChannel)
        else:
        
            print("canal invalido")
        

xxx= tv(5)

xxx.TurnVolumeDown(1)
xxx.TurnVolumeUp(2)
xxx.ChangeChanel(5)




