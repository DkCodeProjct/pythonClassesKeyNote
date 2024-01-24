import random

def main():
    attempts = 4
    numRange = validNum('Enter Num Range: ')

    x = random.randint(1, numRange)

    while attempts > 0:
        guessNum = validNum('guessNum: ')

        if guessNum == x:
            print(f'Won..!\nTheNumIS:[{x}]')
            break
        
        elif guessNum > x:
            print(">X")
            attempts -= 1
        
        else:
            print("<X")
            attempts -= 1
    
    print(f"AttemptsOver: NUM=={x}")

def validNum(prompt):
    while True:
        
        try:
            
            user = int(input(prompt))
            return user
        
        except ValueError:
            pass
if __name__ == "__main__":
    main()