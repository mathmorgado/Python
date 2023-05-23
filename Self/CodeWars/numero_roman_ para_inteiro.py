algarismos_roman = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}


def from_roman(n):
    n = n.upper()
    num = 0

    for alg in ('CM CD XC XL IX IV').split():
        if alg in n:
            num += algarismos_roman[alg]
            n = n.replace(alg, '')

    for alg in ('M D C L X V I').split():
        if alg in n:
            num += n.count(alg) * algarismos_roman[alg]
    
    return num

print(from_roman('MMCMXCVI'))