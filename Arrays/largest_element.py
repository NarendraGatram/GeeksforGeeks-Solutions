'''
    problem : Largest element in the list 
    Difficulty : Easy
'''
def largest(lt,n):
    maximum = lt[0]
    for i in range(1,n):
        if lt[i]>maximum:
            maximum = lt[i]
    return maximum

lt = input('Enter list sepaated by space : ')
lt = list(map(int,lt.split()))
n = len(lt)

print(f'Largest element in the list : {largest(lt,n)}')