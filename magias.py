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

personagem = Personagem("Jorge", 100, 10,12) 
satanas = Inimigo("Satanas", 100, 1, 5,15)
zumbi = Inimigo("Zumbi", 50, 2, 5, 10)

print(personagem.vida)
#personagem.sofrer_dano(20, False)
print(personagem.vida)



class Magia():
    def __init__(self, nome, elemento, ataque, cura):
        self.nome = nome
        self.elemento = elemento
        self.ataque = ataque
        self.cura = cura


def lancar_magia(elemento):              #0Ar #1Fogo #2Terra #3Agua 
    #Ar
    if elemento[0] == 0:
        if elemento[1] == 0:
            magia = Magia("Vento", 0, 15, False)
        elif elemento[1] == 1:
            magia = Magia("Bola de Fogo", 1 , 25, False)
        elif elemento[1] == 2:
            magia = Magia("Projétil de Pedra", 2 , 15, False)
        elif elemento[1] == 3:
            magia = Magia("Seta de Gelo", 3, 15, False)
    #Fogo
    elif elemento[0] == 1:
        if elemento[1] == 0:
            magia = Magia("Bola de Fogo", 1 , 25, False)
        elif elemento[1] == 1:
            magia = Magia("Raio de fogo", 1 , 17, False)
        elif elemento[1] == 2:
            magia = Magia("Meteoro", 2, 25, False)
        elif elemento[1] == 3:
            magia = Magia("Vapor", 3, 15, False)
    #Terra
    elif elemento[0] == 2:
        if elemento[1] == 0:
            magia = Magia("Projétil de Pedra", 2, 15, False)
        elif elemento[1] == 1:
            magia = Magia("Meteoro", 2, 25, False)
        elif elemento[1] == 2:
            magia = Magia("Escudo de Terra", 2, -10, True)
        elif elemento[1] == 3:
            magia = Magia("Lama", 2 , 15, False)
    #Agua
    elif elemento[0] == 3:
        if elemento[1] == 0:
            magia = Magia("Seta de Gelo", 3, 15, False)
        elif elemento[1] == 1:
            magia = Magia("Vapor", 3, 15, False)
        elif elemento[1] == 2:
            magia = Magia("Lama", 2 , 15, False)
        elif elemento[1] == 3:
            magia = Magia("Agua Curativa",3,-20,True)
    
    return magia
    

def combate(personagem,inimigo):
    
    while personagem.vida > 0 and inimigo.vida > 0:
        print("\nVocê está sendo atacado por um "+ str(inimigo.nome)+"!")

        print("|-------------------------------------------|")
        print("| Vida Herói: " + str(personagem.vida))
        print("| Vida " + str(inimigo.nome) + ": " + str(inimigo.vida))
        print("|-------------------------------------------|")
        print("\n1 - Atacar\n\n2 - Fugir \n\n3 - Magia")
        escolha = input("\nQual a sua ação? : ")
        #Ataque
        if int(escolha) == 1:
            dado = random.randint(1,20)
            print("Você rolou: "+str(dado)+" para acertar!")

            if dado == 20:
                inimigo.sofrer_dano(personagem.ataque, True)
                print("Critico! O "+ str(inimigo.nome)+" sofreu " + str(personagem.ataque)+ " de dano")

            elif dado >= inimigo.armadura:
                inimigo.sofrer_dano(personagem.ataque, False)
                print("O "+ str(inimigo.nome)+" sofreu " + str(personagem.ataque)+ " de dano")


            else:                    
                    print("Você errou!")

        #Fugir
        elif int(escolha) == 2:
            dado = random.randint(1,20)
            if dado>5:
                fugir = True
                print("Você Fugiu!")
                return(fugir)
            else:
                    print("Você não conseguiu fugir, agora será atacado!")

        #Magia
        elif int(escolha) == 3:
            print("Você estende as suas mãos para frente e vai conjurar uma magia!")
            x = []
            print("Quais elementos você vai adicionar no seu feitiço?")
            while len(x) <= 1:
                x.append(int(input("0 - Ar \n 1 - Fogo \n 2 - Terra \n 3 - Água\n ")))
            magia = lancar_magia(x)
            print("Você conjurou um " + str(magia.nome))
            if magia.cura == True:
                print(personagem.vida)
                print("Você conjurou uma magia que ira curar/proteger você!")
                personagem.sofrer_dano(magia.ataque, False)
                print("Você recebe " + str(magia.ataque) + " de vida!")
                print(personagem.vida)
            else:
                print("Você conjurou uma magia de ataque!\n O " + str(inimigo.nome) + " vai tentar esquivar!")
                dado = random.randint(1,20)
                print("Para esquiva o inimigo rolou: " + str(dado))
                if dado == 1:
                    print("O " + str(inimigo.nome) + " falha horrivelmente ao esquivar, CRITICO!")
                    critico = int(magia.ataque)
                    inimigo.sofrer_dano(int(magia.ataque), True)
                    print("O "+ str(inimigo.nome)+" sofreu " + str(critico)+ " de dano")

                if dado >= 10:
                    print("O "+ str(inimigo.nome)+" Esquivou e recebe somente metade do dano!")
                    desvio = int(magia.ataque)//2
                    inimigo.sofrer_dano(desvio,False)

                else:
                    print("O " + str(inimigo.nome) + " falha ao esquivar, voce acerta!")
                    inimigo.sofrer_dano(int(magia.ataque), True)
                    print("O "+ str(inimigo.nome)+" sofreu " + str(magia.ataque)+ " de dano")

        #Qualquer Outro
        else:
            print("Escolha uma opção válida!")

        #Ataque do monstro
        if inimigo.vida > 0:
            dado = random.randint(1,20)
            print("O " + str(inimigo.nome) + " vai atacar!")
            if dado == 20:
                print("Crítico!")
                personagem.sofrer_dano(inimigo.ataque,True)
                print("Você toma um golpe muito poderoso que tira "+ str(inimigo.ataque) + " pontos de vida")
            elif dado>personagem.armadura:
                print("Você foi atacado!")
                personagem.sofrer_dano(inimigo.ataque,False)
                print("Você toma um golpe que tira "+ str(inimigo.ataque) + " pontos de vida")
            else:
                print("Você esquivou do golpe!")
        else:
            print("Parabéns! Você venceu o combate!")

def jogo():

    print("Um nobre aventureiro chega as terras de Valak, agora dominadas por um terrivel demonio. Qual será o seu destino")
    nome = input("Digite o nome do seu personagem")
    personagem = Personagem(nome, 100, 10,12) 
    mal = 0
    bem = 0
    vidamax = personagem.vida

    while True:
        print("___________________________________________________________\n Você esta nas estradas, você pode:\n 1 - Acampar \n 2 - Ir para alguma area \n 3 - Inventário ")
        escolha = input("Qual a sua ação? : ")
        if int(escolha) == 1:
            print(personagem.nome)
            sorte = random.randint(1,20)
            if sorte <= 7: 
                print("Você foi atacado no meio do descanço!")
                zumbi = Inimigo("Zumbi", 50, 2, 5, 10)
                combate(personagem,satanas)
            else:
                print("Você descançou e agora se sente revigorado!")
                print(personagem.vida)
                cura = personagem.vida-vidamax
                print("Cura:" + str(cura))
                personagem.sofrer_dano(cura,False)
                print(personagem.vida)
                print(sorte)

        if int(escolha) == 2:
            print("Para onde você quer ir?")
            mortechefe = 0
            if mortechefe < 4: 
                print("1 - |Igreja|\n2 - |Cemitério|\n3 - |Quartel General|\n4 - |Floresta|")
                escolha = int(input(""))
#Igreja
                if escolha == 1:
                    print("Você se aproxima de uma igreja que aparenta ter perdido a sua divindade, agora coberta por vinhas e com as paredes quebradas a igreja se mostra um simbolo de terror")
                    print("Ao entrar na igreja você encontra um monstro mutante de tamanho enorme que outrora poderia ter sido o padre")
                    print("O monstro se vira para você e corre na sua direção")
                    mutante = Inimigo("Mutante",150, 3, random.randint(20,25), 14)
                    combate(personagem, mutante)
                    print("Ao derrotar o mutante, você vê seu corpo no chão, o que você faz?")
                    print("1 - Queimar no lugar em que ele foi derrotado\n2 - Enterrar com uma cerimônia")
                    escolha = int(input(""))
                    if escolha == 1:
                        mal +=1
                        personagem.armadura += 1 
                        print("Do corpo em chamas sai um liquido preto que envolve algumas partes de sua armadura, |ganhou +1 de armadura|")
                    if escolha == 2:
                        bem += 1
                        vidamax += 20
                        print("Você sente que está fazendo o bem por esta região |+20 de vida|") 
            else:
                print("1 - |Igreja|\n2 - |Cemitério|\n3 - |Quartel General|\n4 - |Floresta|\n5 - |Castelo do Mago|")

jogo()
