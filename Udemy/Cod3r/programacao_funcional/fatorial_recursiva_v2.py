# Solução do professor -_-

def fatorial(num):
    return num * (fatorial(num -1) if num -1 > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')