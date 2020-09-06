def fibonacci(m=4_000_000):
    
    """
    
    1 2 3 5 8 13 21
    """
    numbers = [1]
    current = 0
    while current < m:
        current = sum(numbers[-2:])
        numbers.append(current)
        
    return numbers
        
        

def sum_even_fibonnaci():
    return sum(x for x in fibonacci() if x % 2 == 0)


# def solution():
#     return sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])

if __name__ == '__main__':
    print([1][-2:])
    print(fibonacci())
    print(sum_even_fibonnaci())
    