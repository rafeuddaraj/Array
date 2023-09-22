class Array:
    def __init__(self,size=0):
        self.__size = size
        self.__sz = self.__size+10
        self.__value = [None for i in range(self.__sz)]
        self._value = self.__value
    
    @property
    def show(self):
        res = ''
        for i in range(self.__size):
            if i == self.__size-1:
                res = res + str(self.__value[i])
            else:
                res = res + str(self.__value[i]) + ', '
        return f'[{res}]'
    
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self,sz):
        self.__prev = self.__value
        self.__size = self.__size + sz
        self.__sz = self.__size + 10
        
        self.__value = [None for i in range(self.__sz)]
        
        for i in range(len(self.__prev)):
            self.__value[i] = self.__prev[i]
        self._value = self.__value
    @property
    def array(self):
        return self._value[0:self.__size]
    
    def __repr__(self):
        res = ''
        for i in range(self.__size):
            if i == self.__size-1:
                res = res + str(self.__value[i])
            else:
                res = res + str(self.__value[i]) + ', '
        return f'[{res}]'
    

def insertion(arr,size,pos,val):
    for i in range(size,pos-1,-1):
        arr[i+1] = arr[i]
    arr[pos] = val
    return 1

size = int(input("Enter Array Size: "))

arr = Array(size)

for i in range(size):
    arr._value[i] = input('Enter Value: ')
    
pos = int(input('Enter Inserting Position: '))
val = int(input('Enter Inserting Value: '))

arr.size = insertion(arr._value,size,pos,val)

print(arr)
        




