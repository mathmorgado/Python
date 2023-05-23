def solution(n):
    s = ''

    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_rom = ('M CM D CD C XC L XL X IX V IV I').split(' ')

    for i in range(0, len(num)):
        while (n - num[i] >= 0):
            n = n - num[i]
            s += num_rom[i]
    
    return s

print(solution(89))