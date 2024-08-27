# acho q não fiz certo 🤔

class employ:
    def __init__(self, name, salary):
        self.name = str(name)
        self.salary = float(salary)
    
    def showName(self):
        print(self.name)
    
    def showsalary(self):
        print(self.salary)  
          
    def salaryUpgrade(self):
        self.salary += self.salary * 10 /100
        print(self.salary)
    
staley = employ("robeto", "5000")
staley.showName()
staley.showsalary()
staley.salaryUpgrade()
