import os

# Cria uma constante que define a largura da tela como 80 caracteres
TAM_TELA_COL = 80

# Cria uma função que imprime um caracter n vezes
# com base em dois parâmetros:
# o caracter que será impresso e o número de vezes que ele repetirá
def PrintLine(caracter, qtd):
    print(caracter * qtd) 

# Cria uma função que imprime um texto centralizado na tela
def PrintCenter(txt):
    ini = ((TAM_TELA_COL - len(txt)) // 2) + 1
    print((' ' * ini) + txt)

#VARIAVEL QUE ARMAZENARÁ OS CURRÍCULOS
curriculos = []

#Cria um loop que será o fluxo principal do programa
while True:
    
    # Variáveis (Flags) utilizadas para controle de fluxo
    error = False
    continuar = ' '
    
    # Variável que armazenará a quantidade de currículos
    qtd = 0

    # Limpa a tela
    os.system('clear')
    
    # Imprime o cabeçalho do programa
    PrintLine("*", TAM_TELA_COL)
    PrintCenter('ANALISADOR DE CURRÍCULO')
    PrintCenter('DESENVOLVIDO POR ANTONIO VIDAL')
    PrintLine("*", TAM_TELA_COL)
    print('\n')
    
    # Solicita que o usuário defina a quantidade de currículos e armazena o resultado na variável qtd
    qtd = input("DEFINA A QUANTIDADE DE PESSOAS [Máximo 5]: ")

    try:
        # Converte o valor da variável qtd para inteiro
        qtd = int(qtd)
        
        # verifica se o valor está dentro do intervalo válido
        # se não estiver gera uma exceção (erro)
        if (qtd <= 0 or qtd > 5):
            raise ValueError('O número deve estar entre 1 e 5!')

    # Caso algum erro tenha ocorrido,
    # exibe o erro e pergunta se deseja continuar executando o programa    
    except Exception as e:
        error = True
        PrintLine('*', TAM_TELA_COL)
        PrintCenter(f'Ocorreu o erro: {e}')
        PrintLine('*', TAM_TELA_COL)

        while not (continuar in 'sSnN'):
            continuar = input(f'\nDESEJA CONTINUAR? [S/N]: ')

    # Se a resposta foi NÃO, interrompe o programa
    # caso contrario define as flags error como false e continuar como vazio
    # e executa o comando "continue" que pula todos os comandos e volta para o início do loop while
    if continuar in 'nN':
        break
    elif error:
        error = False
        continuar = ' '
        continue

    # Não ocorreu nenhum erro na conversão da variável qtd para inteiro...
    # Limpa a tela 
    os.system('clear')

    # Inicia um loop que será responsável por preencer a lista de currículos
    for c in range(0, qtd):
        PrintLine('-', TAM_TELA_COL) 
        PrintCenter(f'- CURRICULO [{c+1}] -')
        PrintLine('-', TAM_TELA_COL) 
        
        # Preenchimento e validação do nome
        error = True
        while error:
            inName = input("NOME: ")
            if len(inName.strip()) == 0:
                print('\nERRO! Nome não pode ser uma string vazia...')
                continue
            elif len(inName) <= 3:
                print('\nERRO! Nome deve conter mais de 3 caracteres...')
                continue
            elif len(inName) > 30:
                print('\nERRO! Nome não pode conter mais de 30 caracteres...')
                continue
            elif not ''.join(inName.split()).isalpha():
                print('\nERRO! Nome não pode conter números ou caracteres especiais...')
                continue
            else:
                error = False
        
        # Preenchimento e validação da idade
        error = True
        while error:
            inIdade = input("IDADE: ")
            if inIdade.isnumeric() and len(inIdade) > 0 and int(inIdade) >= 6 and int(inIdade) < 120:
                error = False
            else:
                print('\nIDADE INVÁLIDA!')

        # Preenchimento e validadão do sexo
        error = True
        while error:
            inSexo = input("SEXO [F]Feminino [M] Masculino: ").upper()
            if len(inSexo.strip()) > 0 and len(inSexo.strip()) == 1 and inSexo in 'fFmM':
                error = False
            else:
                print('\nSexo preenchido incorretamente!')

        # Todos os campos foram validados!
        # Insere o registro na lista de currículos        
        curriculos.append(
            [inName, int(inIdade), inSexo]
        )

    # Variáveis para exibição do gráfico
    # Média de idade, Maior Idade Masculina e Total de Mulheres
    mediaIdade = 0
    hightManAge = 0
    countWoman = 0

    # Calcula a média de idade:
    for c in range(0, qtd):
        mediaIdade += curriculos[c][1]

    mediaIdade = mediaIdade / qtd

    # Pega o Homem com a maior idade:
    for c in range(0, qtd):
        if (curriculos[c][1] > hightManAge and curriculos[c][2] == 'M'):
            hightManAge = curriculos[c][1]
    
    # Conta quantas mulheres tem nos curriculos
    for c in range(0, qtd):
        if (curriculos[c][2] == 'F'):
            countWoman += 1

    # Limpa a tela
    os.system('clear')
    
    # exibe todos os curriculos
    PrintCenter('\n  -  CURRÍCULOS  -  ')
    for c in range(0, qtd):
        PrintLine('=', TAM_TELA_COL)
        PrintCenter(f'CURRÍCULO Nº {c+1} | NOME: {curriculos[c][0]} | IDADE: {curriculos[c][1]} | SEXO: {curriculos[c][2]}')
    
    PrintLine('=', TAM_TELA_COL)

    # apresenta os resultados
    PrintLine('#', TAM_TELA_COL)
    PrintCenter('-  GRÁFICO  -')
    PrintLine('#', TAM_TELA_COL)
    PrintCenter(f'MÉDIA DE IDADE: {mediaIdade}')
    PrintCenter(f'MAIOR IDADE DO SEXO MASCULINO: {hightManAge}')
    PrintCenter(f'TOTAL DE MULHERES: {countWoman}')
    PrintCenter(f'TOTAL DE HOMENS: {qtd - countWoman}')
    PrintLine('#', TAM_TELA_COL)    

    # pergunta se quer continuar executando o programa
    while not (continuar in 'sSnN'):
        continuar = input('\nDESEJA CONTINUAR? [S/N]:')

    # Se respondeu não
    # interrompe o loop while e vai para o fim do programa
    # se respondeu sim
    # atribui vazio à variável que armazena os currículos
    if continuar in 'nN': 
        break
    else:
        curriculos = []

# Finalização do programa:
# limpa a tela
# imprime a mensagem de encerramento do programa
os.system('clear')
print('Fim da execução!\nAté breve!')

# #FICHA
# for c in range(0, qtd):
#     PrintLine('-', 25)
#     print(f"FICHA [{c}]")
#     name[c] = str(input("NOME: "))
#     idade[c] = str(input("IDADE: "))
#     sexo[c] = str(input("SEXO[F]Feminino[M]Masculino: ").upper())


#     #DADOS INVALIDOS
#     #SEXO
#     sexo[c].strip()
#     if len(sexo[c])>1:
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-              ERRO               -")
#         print("[QUANTIDADE DE CARACTERES EXCEDIDA]")
#         PrintLine('*', 10)
#         sleep(2)
#         break


#     if sexo[c] != 'M' and sexo[c]!='F':
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-     ERRO    -")
#         print("[SEXO INVALIDO]")
#         PrintLine('*', 10)
#         sleep(3)
#         os.system('clear')
#         break
#     #IDADE
#     try:
#         idade1[c] = int(idade[c])
#     except ValueError as err:
#         pass
#     if idade[c].isalpha() == True:
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-        ERRO           -")
#         print("['IDADE' NÃO É CARACTERE]")
#         PrintLine('*', 10)
#         sleep(3)
#         os.system('clear')
#         break
#     if (idade1[c]>120) or (idade1[c]<6):
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-      ERRO    -")
#         print("[IDADE INVALIDA]")
#         PrintLine('*', 10)
#         sleep(3)
#         os.system('clear')
#         break
#     PrintLine('-', 25)
#     sleep(2)
#     #NOME
#     if name[c]=="" or len(name[c])>30 or len(name[c])<3 ==True:
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-     ERRO    -")
#         print("[NOME INVALIDO]")
#         PrintLine('*', 10)
#         sleep(3)
#         os.system('clear')
#         break
#     if any(char.isdigit() for char in name[c])==True:
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-          ERRO         -")
#         print("['NOME' NÃO TEM DECIMAIS]")
#         PrintLine('*', 10)
#         sleep(3)
#         os.system('clear')
#         break
#     if name[c].isalpha() == False or name[c].isalnum() ==False:
#         os.system('clear')
#         PrintLine('*', 10)
#         print("-          ERRO         -")
#         print("['NOME' NÃO TEM CARACTERES ESPECIAIS]")
#         PrintLine('*', 10)
#         sleep(3)
#         os.system('clear')
#         break
#     os.system('clear')
    
# #VARIAVEIS DO GRAFICO    
# media = sum(idade1)/len(idade1)
# idadeMax = 0
# under20woman = 0
# nameIdademax = ''

# #GRAFICO
# for b in range(0,quant):
#     if idade1[b]>idadeMax and sexo[b]=='M':
#         idadeMax = idade1[b]
#         nameIdademax = name[b]
#     if idade1[b]<20 and sexo[b]=='F':
#             under20woman = under20woman + 1
# PrintLine('-', 25)
# print(f"""   
#             -                 GRAFICOS                         -
#             *{PrintLine("*", 50)}                                          * 
#             *MEDIA DE IDADE: {media:2}                           * 
#             *HOMEM COM A MAIOR IDADE: {idadeMax}               * 
#             MULHERES ABAIXO DE 20 ANOS DE IDADE:{under20woman}
#             *{PrintLine("*", 50)}                                          *
#                                 """)