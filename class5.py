
class Cal:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def sub(x,y):
        return x - y
    
    @staticmethod
    def getOp():
        op = int(input('1/2'))
        return op
    
    @classmethod
    def getNum(cls):
        x = int(input('x '))
        y = int(input('y '))
        return x, y
    @classmethod
    def calcult(cls):
        op = cls.getOp()
        x,y = cls.getNum()

        if op == 1:
            print(cls.add(x,y))
        else:
            print(cls.sub(x,y))

        Cal.again()
    @classmethod
    def again(cls):
        doMore = input('doMore ')
        if doMore == 'y':
            Cal.calcult
        elif doMore == 'n':
            print('cc')
        else:   
            Cal.again()

Cal.calcult()
