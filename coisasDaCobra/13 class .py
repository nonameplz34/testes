# acho q não fiz certo 🤔

class employ:
    def __init__(self, name, salary):
        self.name = str(name)
        self.salary = float(salary)
        
        # tbm tem o 
        #  if not isinstance
        #     raise TypeErro
        # mas esse outro é mais rapido kk
    
    def showName(self):
        print(self.name)
    
    def showsalary(self):
        print(self.salary)
    
staley = employ("robeto", "5000")
staley.showName()
staley.showsalary()
