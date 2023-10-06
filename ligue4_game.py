import random
class JogoLigue4:

    def  __init__(self):
        self.time = 'X'
        self.indice_atual = 0
        self.coluna = 0
        self.tela_jogo = [[' ',' ',' ',' ',' ','  ','  '],    # [[00, 01, 02, 03, 04, 05, 06],
                          [' ',' ',' ',' ',' ','  ','  '],    #  [10, 11, 12, 13, 14, 15, 16],
                          [' ',' ',' ',' ',' ','  ','  '],    #  [20, 21, 22, 23, 24, 25, 26],
                          [' ',' ',' ',' ',' ','  ','  '],    #  [30, 31, 32, 33, 34, 35, 36],
                          [' ',' ',' ',' ',' ','  ','  '],    #  [40, 41, 42, 43, 44, 45, 46],
                          [' ',' ',' ',' ',' ','  ','  ']]    #  [50, 51, 52, 53, 54, 55, 56]
        self.tamanho = len(self.tela_jogo)
        self.jogador_atual = 'X'
        self.tipo_jogo = False

    def printar_matriz (self):          #Função para mostrar a matriz ao jogador
        linha = 0
        for linha in self.tela_jogo:
            print(linha)
        return self.tela_jogo

    
    def verificar_empate (self):
        contador_linha = 0
        contador_coluna = 0
        while contador_linha < (self.tamanho - 1):
            contador_coluna = 0
            empate = False
            while contador_coluna < 7:
                if self.tela_jogo[contador_linha][contador_coluna] == ' ':
                    empate = False
                    return empate
                else:
                    empate = True
                contador_coluna = contador_coluna + 1
            contador_linha = contador_linha + 1
        return empate



    def verificar_jogador (self):           #Vericiar se vai ser máquina vs jogador ou jogador vs jogador
        resposta_1 = input('Você quer jogar contra a máquina(S/N)? ')
        if resposta_1 in ['Sim', 'sim', 'S', 's', 'Yes', 'yes', 'Y', 'y']:
            self.tipo_jogo = True
        else:
            self.tipo_jogo = False  
        return self.tipo_jogo          


    def verificar_jogada (self, jogada_valida = False):         #Função que verifica se a jogada é válida
        if self.tipo_jogo == False:
            while jogada_valida == False:
                self.coluna = int(input(f"Digite a coluna que deseja jogar (1-7) (time '{self.jogador_atual}'): "))
                if 7 >= self.coluna >= 0:
                    self.coluna = self.coluna - 1
                    jogada_valida = True
                    return jogada_valida
                else:
                    print('Coluna inválida, escolha uma coluna entre 1 e 7')
                    jogada_valida = False
        if self.tipo_jogo == True:
            if self.jogador_atual == 'X':
                self.coluna = int(input(f"Digite a coluna que deseja jogar (1-7) (time '{self.jogador_atual}'): "))
                if 7 >= self.coluna >= 0:
                    self.coluna = self.coluna - 1
                    jogada_valida = True
                    return jogada_valida
                else:
                    print('Coluna inválida, escolha uma coluna entre 1 e 7')
                    jogada_valida = False
            if self.jogador_atual == 'O':
                self.coluna = random.randint(1,7)
                self.coluna = self.coluna - 1
                jogada_valida = True
                return jogada_valida


    def fazer_jogada (self):            #Função que realiza a jogada
        self.indice_atual = self.tamanho - 1
        while self.indice_atual >= 0:
            if self.tela_jogo[self.indice_atual][self.coluna] == ' ':
                self.tela_jogo[self.indice_atual][self.coluna] = self.jogador_atual
                return self.tela_jogo
            self.indice_atual = self.indice_atual - 1
        if self.indice_atual < 0:
            self.verificar_jogada(False)


    def verificar_coluna(self):         #Verificar vitória na coluna (sempre usando como referência a última jogada)
        if self.indice_atual < 3:
            contador = 1
            linha_baixo = self.indice_atual + 1
            contador_vitoria = 1
            condicao_vitoria = False
            contador_indice = self.indice_atual
            if contador_indice < self.tamanho:
                while contador <= 4:
                    if self.jogador_atual != self.tela_jogo[linha_baixo][self.coluna]:
                        return condicao_vitoria
                    if self.jogador_atual == self.tela_jogo[linha_baixo][self.coluna]:
                        contador_vitoria = contador_vitoria + 1
                    if contador_vitoria == 4:
                        condicao_vitoria = True
                        return condicao_vitoria
                    linha_baixo = linha_baixo + 1
                    contador_indice = contador_indice + 1
                    contador = contador + 1


    def verificar_linha(self):          #Verificar vitória na linha (sempre usando como referência a última jogada)
        contador = 1
        contador_vitoria = 1
        coluna_direita = self.coluna + 1
        coluna_esquerda = self.coluna - 1
        contador_esquerda = True
        contador_direita = True
        condicao_vitoria = False
        if self.coluna == 6:
            coluna_direita = 6
        if coluna_esquerda >= 0 or coluna_direita <=6:
            while contador <= 4:
                if self.jogador_atual != self.tela_jogo[self.indice_atual][coluna_esquerda]:
                    contador_esquerda = False
                if self.jogador_atual != self.tela_jogo[self.indice_atual][coluna_direita]:
                    contador_direita = False
                if contador_esquerda == True:
                    if self.jogador_atual == self.tela_jogo[self.indice_atual][coluna_esquerda]:
                        contador_vitoria = contador_vitoria + 1
                        if (coluna_esquerda - 1) >= 0:
                            coluna_esquerda = coluna_esquerda - 1
                        else:
                            contador_esquerda = False
                        if contador_vitoria == 4:
                            condicao_vitoria = True
                            return condicao_vitoria
                if contador_direita == True:
                    if self.jogador_atual == self.tela_jogo[self.indice_atual][coluna_direita]:
                        contador_vitoria = contador_vitoria + 1
                        if (coluna_direita + 1) <= 6:
                            coluna_direita = coluna_direita + 1
                        else:
                            contador_direita = False
                        if contador_vitoria == 4:
                            condicao_vitoria = True
                            return condicao_vitoria
                contador = contador + 1


    def verificar_diagonal_secundaria(self):        #Verificar vitória na diagonal secundária (sempre usando como referência a última jogada)
        coluna_direita = self.coluna + 1
        if coluna_direita > 6:
            coluna_direita = self.coluna
        linha_cima = self.indice_atual - 1
        coluna_esquerda = self.coluna - 1
        linha_baixo = self.indice_atual + 1
        contador = 1
        contador_vitoria = 1
        contador_cima = True
        contador_baixo = True
        condicao_vitoria = False
        if (coluna_direita <=6 or coluna_esquerda >=0) and (linha_cima >= 0 or linha_baixo <=5):
            while contador <= 4:
                if self.jogador_atual != self.tela_jogo[linha_cima][coluna_direita]:
                    contador_cima = False
                if linha_baixo > 5:
                    linha_baixo = self.tamanho - 1
                if self.jogador_atual != self.tela_jogo[linha_baixo][coluna_esquerda]:
                    contador_baixo = False
                if contador_cima == True:
                    if self.jogador_atual == self.tela_jogo[linha_cima][coluna_direita]:
                        contador_vitoria = contador_vitoria + 1
                        if (linha_cima - 1) >= 0:
                            linha_cima = linha_cima - 1
                            coluna_direita = coluna_direita + 1
                        else:
                            contador_cima = False
                if contador_baixo == True:
                    if self.jogador_atual == self.tela_jogo[linha_baixo][coluna_esquerda]:
                        contador_vitoria = contador_vitoria + 1
                        linha_baixo = linha_baixo + 1
                        coluna_esquerda = coluna_esquerda - 1
                    else:
                        contador_cima = False
                if contador_vitoria == 4:
                        condicao_vitoria = True
                        return condicao_vitoria
                contador = contador + 1


    
    def verificar_diagonal_primaria(self):          #Verificar vitória na diagonal primária (sempre usando como referência a última jogada)
        coluna_direita = self.coluna + 1
        if coluna_direita > 6:
            coluna_direita = self.coluna
        linha_cima = self.indice_atual - 1
        coluna_esquerda = self.coluna - 1
        linha_baixo = self.indice_atual + 1
        contador = 1
        contador_vitoria = 1
        contador_cima = True
        contador_baixo = True
        condicao_vitoria = False
        if (coluna_direita <=6 or coluna_esquerda >=0) and (linha_cima >= 0 or linha_baixo <=5):
            while contador <= 4:
                if self.jogador_atual != self.tela_jogo[linha_cima][coluna_esquerda]:
                    contador_cima = False
                if linha_baixo > 5:
                    linha_baixo = self.tamanho - 1
                if coluna_direita > 6:
                    coluna_direita = 6
                if self.jogador_atual != self.tela_jogo[linha_baixo][coluna_direita]:
                    contador_baixo = False
                if contador_cima == True:
                    if self.jogador_atual == self.tela_jogo[linha_cima][coluna_esquerda]:
                        contador_vitoria = contador_vitoria + 1
                        if (linha_cima - 1) >= 0:
                            linha_cima = linha_cima - 1
                            coluna_esquerda = coluna_esquerda - 1
                        else:
                            contador_cima = False
                if contador_baixo == True:
                    if self.jogador_atual == self.tela_jogo[linha_baixo][coluna_direita]:
                        contador_vitoria = contador_vitoria + 1
                        if (linha_baixo + 1) < 6:
                            linha_baixo = linha_baixo + 1
                            coluna_direita = coluna_direita + 1
                        else:
                            contador_baixo = False
                if contador_vitoria == 4:
                        condicao_vitoria = True
                        return condicao_vitoria
                contador = contador + 1


teste = JogoLigue4()

if teste.verificar_jogador() == False:
    print('Você escolheu jogar contra outro oponente')
    teste.jogador_atual = 'X'
    game_online = True
    while game_online == True:
        #Jogador 1 ('X')
        teste.jogador_atual = 'X'
        if teste.verificar_jogada() == True:        #Se jogada for válida
            teste.fazer_jogada()
            teste.printar_matriz()
            if (teste.verificar_coluna() == True) or (teste.verificar_linha() == True) or (teste.verificar_diagonal_primaria() == True) or (teste.verificar_diagonal_secundaria() == True):
                print(f'O vencedor é o time {teste.jogador_atual}')     #Verificar todos os tipos de vitória
                break
            if teste.verificar_empate() == True:            #Caso o jogo termine empatado
                print('O jogo terminou empatado')
                break

        #Jogador 2 ('O')
        teste.jogador_atual = 'O'
        if teste.verificar_jogada() == True:
            teste.fazer_jogada()
            teste.printar_matriz()
            if (teste.verificar_coluna() == True) or (teste.verificar_linha() == True) or (teste.verificar_diagonal_primaria() == True) or (teste.verificar_diagonal_secundaria() == True):
                print(f'O vencedor é o time {teste.jogador_atual}')     #Verificar todos os tipos de vitória
                break
            if teste.verificar_empate() == True:            #Caso o jogo termine empatado
                print('O jogo terminou empatado')
                break
 
else:
    game_offline = True
    print('Você escolheu jogar contra a máquina')
    while game_offline == True:
        #Jogador 1 ('X')
        teste.jogador_atual = 'X'
        if teste.verificar_jogada() == True:        #Se jogada for válida
            teste.fazer_jogada()
            teste.printar_matriz()
            if (teste.verificar_coluna() == True) or (teste.verificar_linha() == True) or (teste.verificar_diagonal_primaria() == True) or (teste.verificar_diagonal_secundaria() == True):
                print(f'O vencedor é o time {teste.jogador_atual}')     #Verificar todos os tipos de vitória
                break
            if teste.verificar_empate() == True:            #Caso o jogo termine empatado
                print('O jogo terminou empatado')
                break
        
        #Jogador PC ('O')
        teste.jogador_atual = 'O'
        jogada = random.randint(1,7)
        if teste.verificar_jogada(jogada) == True:        #Se jogada for válida
            teste.fazer_jogada()
            print(' ')
            teste.printar_matriz()
            if (teste.verificar_coluna() == True) or (teste.verificar_linha() == True) or (teste.verificar_diagonal_primaria() == True) or (teste.verificar_diagonal_secundaria() == True):
                print(f'O vencedor é o time {teste.jogador_atual}')     #Verificar todos os tipos de vitória
                break
            if teste.verificar_empate() == True:        #Caso o jogo termine empatado
                print('O jogo terminou empatado')
                break
