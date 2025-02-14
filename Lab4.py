# Module 5 Lab (Lab 4)

def fibonacci(num): # Works for now, still not happy with it though
    if num == 0:
        return 0
    elif num == 1:
        return 0
    else:
        sequence = [0,1]
        for i in range(1, num):
            sequence.append((sequence[i]+sequence[i-1]))
            solution = sequence[i-1] + sequence[i-2]
        return solution

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            continue
    return True

def print_prime_factors(num):
    is_not_prime = True
    while is_not_prime:
        if is_prime(num):
            print(f'{num} = {num}')
            break
        factors = []
        prime_factors = []
        for i in range(2,num):
            if num % i == 0:
                factors.append(i)
            else:
                continue
        for i in factors:
            if is_prime(i) is True:
                prime_factors.append(i)
            else:
                continue
        final = []
        for i in prime_factors:
            result = num / i
            while result % i == 0:
                result = result / i
                final.append(i)
                continue
            else:
                final.append(i)
        last = final.pop()
        print(f'{num} = ', end='')
        for i in final:
            print(f'{i} * ', end='')
        print(last)
        break



