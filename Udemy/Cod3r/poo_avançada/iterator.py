class RGB:
    def __init__(self) -> None:
        self.cores = ['Red', 'Green', 'Blue'][::-1] # Inverte a ordem para interar com o pop()

    def __iter__(self): # Objeto interável
        return self
    
    def __next__(self): # Interator    
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()
    

if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('\nACABOU\n')

    for cor in RGB():
        print(cor)
    

