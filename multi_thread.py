import time

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(2)
        print('square: ',n*n, time.time())

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(2)
        print("cube: ",n*n*n, time.time())

arr=[2,3,8,9]

t=time.time()
calc_square(arr)
calc_cube(arr)