#Lab bonus
def patter(number:int):
    '''This function prints a pattern of numbers based on the input number.'''
    for i in range(number, 0, -1):
        for j in range(i):
            print(i-j, end=' ')
        print()

result = 5
patter(result)
