class Carro:
    def __init__(self, vel_max=200):
        self.vel = 0
        self.vel_max = vel_max
    

    def acelerar(self, delta):
        if self.vel + delta > self.vel_max:
            self.vel = self.vel_max
        else:
            self.vel += delta

        return self.vel

    
    def frear(self, delta):
        if self.vel - delta < 0:
            self.vel = 0
        else:
            self.vel -= delta
        
        return self.vel


if __name__ == '__main__':
    c1 = Carro(180)  # Velocidade máxima

    for _ in range(25):
        print(c1.acelerar(delta=8))
    
    for _ in range(10):
        print(c1.frear(delta=20))
