class Isvalid:
    def __init__(self,inputStr):
        self.input = inputStr
    
    def isValid(self):
        if self.input[0].isupper() == False or self.input[1].isupper() == False:
            return False
        if len(self.input) < 2 or len(self.input) > 6:
            return False
        for c in self.input:
            if c in [' ', '?', '!', '#']:
                return False
        return True
    def __str__(self):
        return f"Input: {self.input}"
def main():
    user = input('EnterVantyPlate: ')
    isvalid = Isvalid(user)
    if isvalid.isValid():
        print('valid')
    else:
        print('invlaid')
if __name__ == "__main__":
    main()