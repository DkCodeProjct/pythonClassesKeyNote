import random

class LittleProf:
    
    def __init__(self):
        self.score = 0
    
    def getLevel(self):
        
        while True:
            try:
                
                level = int(input("chooseLevel[1/2/3] "))
                if level in [1,2,3]:
                    return level
                else:
                    print("level wasn't in [1/2/3]")
            
            except ValueError:
                pass
    
    def genNum(self,level):
        
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        
        elif level == 2:
            x = random.randint(9,99)
            y = random.randint(9,99)
        
        else:
            x = random.randint(99,999)
            y = random.randint(99,999)
        
        return x, y
    
    def simulateRound(self,x,y):
        
        attempts = 3
        
        while attempts > 0:
            getAns = int(input(f'{x}+{y}== '))
            
            if getAns == (x+y):
                return True
            
            else:
                print("EEE")
                attempts -= 1
    
    def simulateGame(self,level,round=10):
        
        for _ in range(round):
            
            x,y = self.genNum(level)
            if self.simulateRound(x,y):
                print("correct")
                self.score += 1
            else:
                print('EEE')
        return self.score
    
    def main(self):
        level = self.getLevel()
        self.simulateGame(level)
        print(f"score:{self.score}")

if __name__ == "__main__":
    prof = LittleProf()
    prof.main()