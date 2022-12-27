class Carro:
    def __init__(self, vel_max):
        self.velocidade_atual = 0
        self.vel_max = vel_max
    

    def acelerar(self, delta):
        vel_maxima = self.vel_max
        vel_nova = self.velocidade_atual + delta
        self.velocidade_atual = vel_nova if vel_nova <= vel_maxima else vel_maxima

        return self.velocidade_atual

    
    def frear(self, delta):
        vel_nova = self.velocidade_atual - delta
        self.velocidade_atual = vel_nova if vel_nova >= 0 else 0
        
        return self.velocidade_atual


if __name__ == '__main__':
    c1 = Carro(180)  # Velocidade máxima

    for _ in range(25):
        print(c1.acelerar(delta=8))
    
    for _ in range(10):
        print(c1.frear(delta=20))
