def soma (*args): # Empacota uma série de elementos dentro de uma tupla. Convenção de usar 'args' 
    return sum(args)


soma_15 = soma(1, 2, 3, 4, 5) # Empacotamento 

print(soma_15)

nums = 1, 2, 3, 4, 5

# outra_soma = soma(nums) Empacota uma tupla dentro de outra tupla, dando erro ao chamar a função 'sum' -> ((1, 2, 3, 4, 5),)

outra_soma = soma(*nums) # Desempacota todos os elementos presentes na varivel/tuple 'nums'. Distribui eles.

print(outra_soma)