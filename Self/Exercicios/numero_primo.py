def is_prime(num):
    if num <= 1 or (num != 2 and num % 2 == 0):
        return False

    for c in range(3, int(num**.5)+1, 2):
        if num % c == 0:
            return False
    
    return True

print(is_prime(73))