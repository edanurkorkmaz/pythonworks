def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

def prime_numbers():
    for num in range(1, 1001):
        if is_prime(num):
            print(num, end=" ")

def perfect_numbers():
    for num in range(1, 1001):
        if is_perfect(num):
            print(num, end=" ")

def decorator(func):
    def wrapper():
        print("Asal Sayılar:")
        func()
        print("\nMükemmel Sayılar:")
        perfect_numbers()
    return wrapper

@decorator
def prime_and_perfect_numbers():
    prime_numbers()

prime_and_perfect_numbers()