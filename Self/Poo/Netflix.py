class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ['basic', 'premium']
        
        if plano.lower() in self.lista_plano:
            self.plano = plano.lower()
        else:
            print('Plano inválido!')
        
    def mudar_plano(self, novo_plano):
        if novo_plano.lower() != self.plano and novo_plano in self.lista_plano:
            self.plano = novo_plano
            return novo_plano
        else:
            print('plano inválido!')
    
    def ver_filme(self, filme, plano_filme):
        if plano_filme.lower() == self.plano:
            return(f'Ver {filme}')
        else:
            return('Plano para filme inválido!')


cliente1 = Cliente('Matheus', 'matheus@gmail.com', 'basic')

print(f'Nome: {cliente1.nome}')

print(f'\nMeu plano: {cliente1.plano}\n'
      f'Tentando ver Pica-Pau: {cliente1.ver_filme("Pica Pau", "premium")}\n')

print(f'Novo plano: {cliente1.mudar_plano("premium")}')

print(f'\nMeu plano: {cliente1.plano}\n'
      f'Tentando ver Pica-Pau: {cliente1.ver_filme("Pica Pau", "premium")}\n')

cliente2 = Cliente('Alex', 'alex@gmail.com', 'premium')

print(f'Nome: {cliente2.nome}')

print(f'\nMeu plano: {cliente1.plano}\n'
      f'Tentando ver Pica-Pau: {cliente1.ver_filme("Pica Pau", "premium")}\n')




