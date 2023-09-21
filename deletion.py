# 0 1 2 3 4 5
# 1 2 4 5 6 7

# add position 2 value 3

# 0 1 2 3 4 5 6
# 1 2 4 4 5 6 7

size = int(input('Enter Size: '))

arr = [0 for i in range(size+5)]

for i in range(size):
    arr[i] = int(input('Enter Value: '))

print(arr)

pos = int(input('Enter Inserting Position: '))
flag = True
if pos < size:
    flag = False
    for i in range(pos,size):
        arr[i] = arr[i+1]

    size = size-1
elif pos > size:
        print('position is not valid')

if not flag:
    print('[',end='')
    for i in range(size):
        if i == size-1:
            print(arr[i],end='')
        else:
            print(arr[i],end=', ')
            
    print(']')