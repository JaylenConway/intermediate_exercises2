import time
import random

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if __name__ == '__main__':
    n = random.randint(15, 35)
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f'The {n}th term in the fibonacci sequence is {result}')
    print(f'Time taken: {end_time - start_time:.6f} seconds')