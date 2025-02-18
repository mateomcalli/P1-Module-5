# Module 5 Lecture Activities

def fourbonacci(n):
    a,b,c,d = 1,4,7,8
    for i in range(n-1):
        seq = 4*a + 3*b + 2*c + d
        a = b
        b = c
        c = d
        d = seq
    print(a)

# fourbonacci(0)

def odd_squares(n):
    for i in range((n*2)+1):
        attempt = i * i
        if attempt % 2 == 1:
            print(attempt)

# odd_squares(15)

def diamond(n):
    for i in range(1, n+1):
        length_from_middle = abs(n//2 - (i-1))
        print(' ' * length_from_middle, end='')
        for j in range(1, n - (2 * length_from_middle) + 1):
            print(j, end='')
        print()

# diamond(7)