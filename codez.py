class Account:
    def __init__(self):
        self._balance :float= 0
    
    def Deposite(self,n):
        self._balance += n
   
    def Withdraw(self,n):
        if self._balance < 500:
            print('500$ bank tax.')
        self._balance -= n
    
    @property
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f'blance:{self._balance}$'    

def main():
    account = Account()
    try:
        deposit :float = float(input('d '))
        withdraw :float = float(input('w '))
    
    except ValueError:
        pass
    
    else:
        account.Deposite(deposit)
        account.Withdraw(withdraw)
    print(account)

if __name__ == "__main__":
    main()