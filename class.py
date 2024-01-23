class Sidemen:
    
    def __init__(self, name, country, age, youTube):
        self.name = name
        self.country = country
        self.age = age
        self.youTube = youTube
    
    def __str__(self):
        return f"-- {self.name} is from {self.country},, AGE::{self.age} And his youTubeChannel is {self.youTube} --"
        
def main():
    sidemen = getSidemen()
    print(sidemen)

def getSidemen():
    name = input("Name: ").title()
    country = input('Country: ')
    age = int(input('Age: '))
    youTube = input('YouTube: ')
    return Sidemen(name, country, age, youTube)

if __name__ == "__main__":
    main()