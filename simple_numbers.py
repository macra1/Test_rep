"""
Простые числа
"""

def is_simple(n):
    for elem in range(2, n):
        if n % elem == 0:
            return False
    return True
        

if __name__ == "__main__":        
    # Выводим простые числа:
    for i in range(500):
        if is_simple(i):
            print(i, end=" ")
    # Вроде работает :)
