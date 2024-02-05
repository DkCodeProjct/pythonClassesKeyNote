class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError('EmptyJar')
        
        else:
            self._capacity = capacity
            self._size = 0
        
    def __str__(self):
        return self._size * '*'
   
    def deposite(self,n):
        if n > self._capacity:
            raise ValueError('JarIsFull')
        
        if n + self._size > self._capacity:
            raise ValueError('JarIsFull')
        
        self._size += n
   
    def withdraw(self,n):
        if self._size < n:
            raise ValueError('JarIsEmpty')
       
        self._size -= 1
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size
    
jar = Jar()
jar.deposite(3)
jar.withdraw(1)
print(jar)