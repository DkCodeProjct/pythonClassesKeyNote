from datetime import date

#calculate howManyMinYou'veBeenLive ---.> (365*24*60)*(yearLive)={Min}
    #BUT there is 366 daysForSomeYear// that's why we need datetime library 
        #BUT this is justAPsudoCode for WritingTheFuncionalCode..//
class Life:
    def __init__(self):
        
        self.days = 365
        self.hours = 24
        self.min = 60
        self.years = int(input('howManyYearsHaveYouBeenLive: '))
    
    def Calculate(self):
        
        result = self.days * self.hours * self.min * self.years
        print(f"YouHaveLived: {result}-min")

if __name__ == "__main__":
    life = Life()
    life.Calculate()
        