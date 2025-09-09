'''
    Finding the Largest and smallest element in the list
'''
def largestAndSmaller(lt,n):
    minimum = lt[0]
    maximum = lt[0]

    for i in range(1,n):
        if lt[i]>maximum:
            maximum = lt[i]
        if lt[i]<minimum:
            minimum = lt[i]
    print(f'Largest element in the list : {maximum}')
    print(f'Smallest element in the list : {minimum}')

lt = input('Enter list sepaated by space : ')
lt = list(map(int,lt.split()))
n = len(lt)
largestAndSmaller(lt,n)