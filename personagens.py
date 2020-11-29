import random

class Personagem():
    def __init__(self, nome, vida, ataque, armadura):
        self.nome = nome
        self.vida =  vida
        self.ataque = ataque
        self.armadura = armadura

    def sofrer_dano(self,dano,critico):
        if critico:
            self.vida -= 2*dano
        else:
            self.vida -= dano

class Inimigo():
    def __init__(self, nome, vida, elemento, ataque, armadura):
        self.nome = nome
        self.vida =  vida
        self.elemento = elemento
        self.ataque = ataque
        self.armadura = armadura

    def sofrer_dano(self,dano,critico):
        if critico:
            self.vida -= 2*dano
        else:
            self.vida -= dano


satanas = Inimigo("Satanas", 100, 1, 5,15)
