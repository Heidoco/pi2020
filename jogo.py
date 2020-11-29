import random
from personagens import *



def explorar_igreja(personagem,bem,mal,vidamax):
    print("Você se aproxima de uma igreja que aparenta ter perdido a sua divindade, agora coberta por vinhas e com as paredes quebradas a igreja se mostra um simbolo de terror")
    print("Ao entrar na igreja você encontra um monstro mutante de tamanho enorme que outrora poderia ter sido o padre")
    print("O monstro se vira para você e corre na sua direção")
    mutante = Inimigo("Mutante",150, 3, random.randint(20,25), 14)
    resultado = combate(personagem, mutante)

    if resultado:
        return False

    if personagem.vida > 0:
        print("Ao derrotar o mutante, você vê seu corpo no chão, o que você faz?")
        print("1 - Queimar no lugar em que ele foi derrotado\n2 - Enterrar com uma cerimônia")
        escolha = int(input(""))
        if escolha == 1:
            print("Do corpo em chamas sai um liquido preto que envolve algumas partes de sua armadura, |ganhou +1 de armadura|")
            return 1

        if escolha == 2:
            print("Você sente que está fazendo o bem por esta região |+20 de vida|")
            return 2

    else:
        print("Você morre no combate contra o mutante.")
        return False

def explorar_quartel(personagem,bem,mal,vidamax):
    print("Você se aproxima do que outrora fora um quartel general da cidade.")
    print("Ao entrar você encontra diversos corpos jogados no chão e 10 soldados com olhos demoniacos olhando para você\n O lider se move em sua direção!")
    general = Inimigo("General", random.randint(150,200),2,random.randint(20,30),16)
    combate(personagem,general)

    if personagem.vida > 0:
        print("Ao derrotar o general, os seus subordinados saem correndo e o corpo desaparece, exceto por uma espada e um escudo")
        print("1 - Pegar a espada\n2 - Pegar o escudo")
        escolha = int(input(""))
        if escolha == 1:
            print("A espada é grande mas você consegue levantar |+5 de ataque|")
            return 1

        if escolha == 2:
            print("O escudo é feito de aço e agora você está mais seguro |+2 de armadura|")
            return 2

    else:
        print("Você morre no combate contra o General.")
        return False

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
        print("|1 - Atacar\n|2 - Fugir \n|3 - Magia")
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
                x.append(int(input("*0 - Ar \n*1 - Fogo \n*2 - Terra \n*3 - Água\n ")))
            magia = lancar_magia(x)
            if magia.cura == True:
                print(personagem.vida)
                print("Você conjurou uma magia que ira curar/proteger você!")
                print("Você conjurou um " + str(magia.nome))
                personagem.sofrer_dano(magia.ataque, False)
                print("Você recebe " + str(magia.ataque) + " de vida!")
                print(personagem.vida)
            else:
                print("\nVocê conjurou um " + str(magia.nome))
                print("Você conjurou uma magia de ataque!\nO " + str(inimigo.nome) + " vai tentar esquivar!")
                dado = random.randint(1,20)
                print("Para esquiva o inimigo rolou: " + str(dado))
                if dado == 1:
                    print("O " + str(inimigo.nome) + " falha horrivelmente ao esquivar, CRITICO!")
                    critico = 2*int(magia.ataque)
                    inimigo.sofrer_dano(int(magia.ataque), True)
                    print("O "+ str(inimigo.nome)+" sofreu " + str(critico)+ " de dano")
                    

                elif dado >= 10:
                    print("O "+ str(inimigo.nome)+" Esquivou e recebe somente metade do dano!")
                    desvio = int(magia.ataque)//2
                    inimigo.sofrer_dano(desvio,False)
                    print("O "+ str(inimigo.nome)+" sofreu " + str(desvio) + " de dano")
                    
                elif dado < 10 and dado > 1:
                    print("O " + str(inimigo.nome) + " falha ao esquivar, voce acerta!")
                    inimigo.sofrer_dano(int(magia.ataque), False)
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

    print("|Um nobre aventureiro chega as terras de Valak, agora dominadas por um terrivel demonio. Qual será o seu destino?")
    nome = input("|Digite o nome do seu personagem: ")
    personagem = Personagem(nome, 100, 10,12) 
    mal = 0
    bem = 0
    igreja = False
    quartel = False
    vidamax = personagem.vida
    mortechefe = 0

    while True:

        print("|------------------------------------------------|\n| Você ja limpou " + str(mortechefe) + " áreas\n| Você esta nas estradas, você pode:\n| 1 - Acampar \n| 2 - Ir para alguma area \n| 3 - Status \n|------------------------------------------------|")
        escolha = input("Qual a sua ação? : ")
        if int(escolha) == 1:
            print(personagem.nome)
            sorte = random.randint(1,20)
            if sorte <= 7: 
                print("Cuidado "+str(personagem.nome)+"! Você foi atacado no meio do descanço!")
                zumbi = Inimigo("Zumbi", 50, 2, 5, 10)
                combate(personagem,zumbi)
            else:
                print("Você descançou e agora se sente revigorado!")
                cura = personagem.vida-vidamax
                print("Cura:" + str(cura))
                personagem.sofrer_dano(cura,False)
                print(sorte)

        if int(escolha) == 2:
            print("Para onde você quer ir?")
            if mortechefe < 2: 
                print("1 - |Igreja|\n2 - |Cemitério|\n3 - |Quartel General|\n4 - |Floresta|")
                lugar = int(input(""))
#Igreja
                if lugar == 1:
                    if igreja:
                        print("Você ja passou por aqui e tudo continua igual!")
                        pass
                    else:
                        estado = explorar_igreja(personagem,bem,mal,vidamax)
                        if estado:
                            igreja = True
                            mortechefe += 1
                            if estado == 1:
                                mal +=1
                                personagem.armadura += 1 
                            if estado == 2:
                                bem +=1
                                vidamax += 20
                        else:
                            return False
#Quartel General
                if lugar == 3:
                    if quartel:
                        print("Você ja passou por aqui e tudo continua igual!")
                        pass
                    else:
                        estado = explorar_quartel(personagem,bem,mal,vidamax)
                        if estado:
                            quartel = True
                            mortechefe += 1
                            if estado == 1:
                                mal +=1
                                personagem.ataque += 5 
                            if estado == 2:
                                bem +=1
                                personagem.armadura += 2
                        else:
                            return False
            else:
                print("1 - |Igreja|\n2 - |Cemitério|\n3 - |Quartel General|\n4 - |Floresta|\n5 - |Castelo do Mago|")

        if int(escolha) == 3:
            print("|------------------------------------------------|")
            print("|Nome: "+str(personagem.nome))
            print("|Vida: "+str(vidamax)+" / "+str(personagem.vida))
            print("|Armadura: " + str(personagem.armadura))
            print("|Dano:" + str(personagem.ataque))
            print("|Areas completas:" + str(mortechefe))
            print("|------------------------------------------------|")
            input("1 - Sair")


if __name__ == "__main__":
    jogo()
