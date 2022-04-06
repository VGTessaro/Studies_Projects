# numero total de pecas no tabuleiro
n_tot = 1
# maximo numero de pecas por jogada
m = 1
# jogada do usuario

def usuario_escolhe_jogada(n,m):
    global n_tot
    usu_joga = int(input("\nQuantas pacas voce quer tirar?\n"))
    if usu_joga < m:
        return usu_joga
    while usu_joga < 1 or usu_joga > 3:
        print("Oops! Jogada inválida! Tente de novo.\n")
        usu_joga = int(input("\nQuantas pacas voce quer tirar?\n"))
    return usu_joga
    print("Voce retirou", usu_joga," pecas")
    n_tot = n - usu_joga
    print("Restam", n_tot," pecas no tabuleiro")
    return n_tot

# jogada do computador
# a estratégia do computador para ganhar consiste em deixar sempre
    # um número de peças que seja múltiplo de (m+1) ao jogador.
    # Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

def computador_escolhe_jogada(n, m):
    global n_tot
    if n <= m:
        return n
    if n <= 3 and n >= 1:
        n_tot = n
        return n_tot
    else:
        n_tot = n % (m+1)
        if n_tot > 0:
            return n_tot
        else:
            return m

""" selecao de quem comeca
como a mecanica do jogo ocorre
somatoria de score"""
def partida():
    n = int(input('Quantas peças?\n'))
    m = int(input('Limite de peças por jogada?\n'))
    turno_com = False
    if n % (m + 1) == 0:
        print('Você começa!')

    else:
        print('Computador começa!')
        turno_com = True

    while n > 0:
        if turno_com == True:
            peca = computador_escolhe_jogada(n, m)
            turno_com = False
            print("\nO computador tirou", peca, " peça(s)")
            n = n - peca
            print("Agora restam", n, " peças no tabuleiro.")
        else:
            peca = usuario_escolhe_jogada(n,m)
            turno_com = True
            print("\nVocê tirou", peca, " peça(s)")
            n = n - peca
            print("Agora restam", n, " peças no tabuleiro.")

    print("Fim do jogo! O computador ganhou!")





def campeonato():

    print("**** Rodada 1****")
    partida()
    placar = 1
    print("Placar: Você 0 X ",placar," Computador")

    print("**** Rodada 2****")
    partida()
    placar += 1
    print("Placar: Você 0 X ",placar," Computador")
    print("**** Rodada 3****")
    partida()
    placar += 1
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X ",placar," Computador")


# determinando tipo de partida e quantas rodadas tera o campeonato
# quantas pecas tem no jogo
# qual o limite de pecas permitido para retirada

def inicio_jogo():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    j = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))
    a = 1
    b = 2
    while j != a and j != b:
        j = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))

    if j == a:
        print("Você escolheu uma partida!")
        ## criar while para impedir erro por caracter errado ou vazio
    # while n != int or n != num:
        #   n = int(input('Numero invalido. Quantas peças?\n'))
        #  break
        partida()
    else:
        if j == b:
            print("Você escolheu um campeonato!")
            campeonato()


inicio_jogo()