def solution(s):
    pares = []
    print('oi')
    
    if len(s) % 2 != 0:
        s += '_'
    
    for i in range(0, len(s), 2):
        pares.append(s[i:i+2])
    
    print( pares )


solution('stredsfxn')
