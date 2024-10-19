#  0 = PEDRA
#  1 = PAPEL
#  2 = TESOURA

# Possíveis resultados
# EMPATAR [E]
# PERDER  [P]
# GANHAR  [G]

#  #############################################################
#   TABELA DE RESULTADOS POSSÍVEIS DO PONTO DE VISTA DO USUÁRIO
#  #############################################################
#                COMPUTADOR (AI):
#                  0     1     2   
#   USUÁRIO:  0 |  E  |  P  |  G  |
#             1 |  G  |  E  |  P  |
#             2 |  P  |  G  |  E  |

import random
# Biblioteca para funções nativas do sistema
import os

# Lista de resultados possíveis criada com base na tabela de resultados
combinacoes = [
    ['NÓS DOIS ESCOLHEMOS PEDRA!\nNÓS EMPATAMOS!!!','MEU PAPEL EMBRULHA SUA PEDRA!\nVOCÊ PERDEU!!!' ,'SUA PEDRA QUEBRA MINHA TESOURA!\nVOCÊ GANHOU!!!' ],
    ['SEU PAPEL EMBRULHA MINHA PEDRA!\nVOCÊ GANHOU!!!' ,'NÓS DOIS ESCOLHEMOS PAPEL!\nNÓS EMPATAMOS','MINHA TESOURA CORTA SEU PAPEL!\nVOCÊ PERDEU!!!' ],
    ['MINHA PEDRA QUEBRA SUA TESOURA!\nVOCÊ PERDEU' ,'SUA TESOURA CORTA MEU PAPEL!\nVOCÊ GANHOU' ,'NÓS DOIS ESCOLHEMOS TESOURA!\nNÓS EMPATAMOS'],
]

# Lista usada para exibir as escolhas
descricoes = ['PEDRA', 'PAPEL', 'TESOURA']

# Cria a variável que mostar o número de rodadas e inicializa ela com o valor 0
rodadas = 0

# Cria a variável que armazenará os erros
error = ''

# Acumuladores do Placar
winnerAI = 0
winnerUser = 0
empates = 0

# loop principal
while(True):
  # limpa a tela. Use 'clear' se estiver num prompt LINUX e 'cls' se estiver num prompt DOS/WINDOS
  os.system('clear')
  # Computador faz sua escolha aleatória
  escolhaAI = random.choice([0,1,2])
  # try except: tratamento de erro caso o usuário digite uma letra no lugar de um número, por exemplo
  try:
    # Exibe o menu com as opções e pega a escolha do usuário no prompt
    escolhaUsuario = int(input(error.upper() + "\n\nEu já fiz minha escolha! Agora faça a sua!\n\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\n[3] Sair do jogo\n\nDigite um dos números acima: "))

    # Reinicia a variável que contém os erros
    error = ''
    
    # Se o usuário escolheu 0, 1 ou 2, ou seja: se a escolha for diferente de 3 joga
    if (escolhaUsuario != 3):
      # incrementa o contador de partidas
      rodadas += 1
      # define o resultado baseado na lista de combinações possíveis
      resultado = combinacoes[escolhaUsuario][escolhaAI]
      # atualiza o placar
      if ('VOCÊ PERDEU' in resultado):
        winnerAI += 1
      elif ('VOCÊ GANHOU' in resultado):
        winnerUser += 1
      else:
        empates += 1
      # exibe o resultado na tela
      print(f'\n\nVOCÊ ESCOLHEU {descricoes[escolhaUsuario]} E EU ESCOLHI {descricoes[escolhaAI]}\n{resultado}')
      # armazena a escolha do usuário (se quer continuar jogando) na variável 'question'
      question = input('\n\nDESEJA CONTINUAR JOGANDO? S/N\n')
      # se o usuário digitou n ou N (não) finaliza o loop
      if (question in 'Nn'):
        break
    # o usuário escolheu a opção 3 (sair do jogo). Finaliza o loop
    else:
      break
  
  # exibe uma mensagem de erro caso o usuário digite uma letra no lugar de um número
  except ValueError:
    error  = 'Você digitou um valor inválido!'

# limpa a tela
os.system('clear')
# exibe a mensagem de saída com o placar do jogo!
print(f'Obrigado por jogar comigo!\n\nTotal de rodadas = {rodadas}\nNosso placar: VOCÊ: {winnerUser} | EU: {winnerAI} | EMPATES: {empates}')

# # CÓDIGO DO ANTõNIO
# import random
# pedra = 1
# papel = 2
# tesoura = 4
# escolha = int(input(" [1] PEDRA\n [2] PAPEL\n [3] TESOURA\nEscolha:"))

# escolhaAi = [pedra, papel, tesoura]
# escolha2 = random.choice(escolhaAi)
# print(f"Escolha da AI = {escolha2} ")
# resultado = escolha - escolha2

# ##Usuario ganha
# if resultado==-3:
#     print("YOU: PEDRA VS AI: PAPEL")
#     print("PEDRA ganhou(YOU)")
# elif resultado == 2:
#     print("YOU: TESOURA VS AI: PAPEL")
#     print("TESOURA ganhou(YOU)")
# elif resultado == 1:
#     print("YOU: PAPEL VS AI: PEDRA")
#     print("PAPEL ganhou(YOU)")
# ##Empate
# elif resultado == 0:
#     if escolha ==1:
#         print("YOU: PEDRA VS AI: PEDRA")
#         print("Empate")
#     elif escolha ==2:
#         print("YOU: PAPEL VS AI: PAPEL")
#         print("Empate")
#     elif escolha ==3:
#         print("YOU: TESOURA VS AI: TESOURA")
#         print("Empate")
# ##Maquina ganha
# elif resultado==3:
#     print("YOU: TESOURA VS AI: PEDRA")
#     print("PEDRA ganhou(AI)")
# elif resultado == -2:
#     print("YOU: PAPEL VS AI: TESOURA")
#     print("TESOURA ganhou(AI)")
# elif resultado == -1:
#     print("YOU: PEDRA VS AI: PAPEL")
#     print("PAPEL ganhou(AI)")
# else:
#     print("Valor invalido, tente novamente!")