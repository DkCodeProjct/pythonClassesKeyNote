import random

class Num:
    def __init__(self):
        
        self.attempts = 5
        self.num1 = self.isValid('enterNumRng1 ')
        self.num2 = self.isValid('enterNumRng2 ')
        self.X = random.randint(self.num1, self.num2)
    
    def Game(self):
        
        while self.attempts > 0:
            getNum = self.isValid('guessNum[X] ')
            
            if getNum == self.X:
                print(f'...WON... \nX==[{self.X}]')
                break
           
            elif getNum > self.X:
                print('>X')
            
            else:
                print('<X')
    
    def isValid(self, prompt):
        
        while True:
            try:
                user = int(input(prompt))
                return user
            except ValueError:
                pass

if __name__ == "__main__":
    
    game = Num()
    game.Game()