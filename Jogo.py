class Jogador():
    def __init__(self, nome, vida, ataque, mana):
        self.nome = nome
        self.vida =  vida
        self.ataque = ataque
        self.mana = mana
    def sofrer_dano(self,vida,dano):
        vida = vida-dano
        return vida
def lancar_magia(elemento):              #0Ar #1Fogo #2Terra #3Agua 
    #Ar
    if elemento[0] == 0:
        if elemento[1] == 0:
            return "Vento"
        elif elemento[1] == 1:
            return "Bola de Fogo"
        elif elemento[1] == 2:
            return "Projétil de Pedra"
        elif elemento[1] == 3:
            return "Gelo"
    #Fogo
    elif elemento[0] == 1:
        if elemento[1] == 0:
            return "Bola de Fogo"
        elif elemento[1] == 1:
            return "Raio de fogo"
        elif elemento[1] == 2:
            return "Meteoro"
        elif elemento[1] == 3:
            return "Vapor"
    #Terra
    elif elemento[0] == 2:
        if elemento[1] == 0:
            return "Projétil de Pedra"
        elif elemento[1] == 1:
            return "Meteoro"
        elif elemento[1] == 2:
            return "Escudo de Terra"
        elif elemento[1] == 3:
            return "Lama"
    #Agua
    elif elemento[0] == 3:
        if elemento[1] == 0:
            return "Seta de Gelo"
        elif elemento[1] == 1:
            return "Vapor"
        elif elemento[1] == 2:
            return "Lama"
        elif elemento[1] == 3:
            return "Agua Curativa"

x = [3,3]
print(lancar_magia(x))