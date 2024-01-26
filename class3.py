class Cockprice:
    def __init__(self):
        
        self.attempts = 4
        self.validCoin = [10,20,5]
        self.price = 50
        self.payment = 0

    def cockMachine(self):
        
        while self.payment < self.price:
            getCoin = self.isValid('enterCoin:[20/10/5] ')
            
            if getCoin in self.validCoin:
                self.payment += getCoin
            
            else:
                print('invlaidCoin')
            
           
            if self.payment >= self.price:
                change = self.payment - self.price
                print(f"------payementSuccess------\nyourChange:{change}")
            
            else:
                print(f'NEED; {self.price-self.payment}')


    def isValid(self,prompt):
        
        while True:
            try:
                user = int(input(prompt))
                return user
            except ValueError:
                pass

if __name__ == "__main__":
    cock = Cockprice()
    cock.cockMachine()