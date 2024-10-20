import os

flag = True

while (flag):
  numPrimos = []
  os.system('clear')
  count = input('Até quantos números primos usarei para decompor (de 1 a ...)?\nDigite o intervalo final: ')
  
  try:
    count = int(count)

    # ENCONTRANDO OS NÚMEROS PRIMOS DO INTERVALO
    for c in range(1, count + 1):
      i = 0
      n = 1
      
      # VERIFICA QUANTAS VEZES
      # O NÚMERO PODE SER DIVIDIDO SEM SOBRAR RESTO DE DIVISÃO
      for n in range(1, c + 1):
        if (c % n) == 0:
          i += 1
      
      # CASO O NÚMERO SÓ POSSA SER DIVIDIDO SEM SOBRAR RESTO DE DIVISÃO
      # APENAS DUAS VEZES, ENTÃO ELE É UM NÚMERO PRIMO
      # ADICIONA ELE NA LISTA DE NÚMEROS PRIMOS.
      if (i == 2):
        numPrimos.append(c)

    print(f'\nNumeros Primos encontrados no intervalo: {numPrimos}')

    # PROCESSO DE FATORAÇÃO:
    while (flag):
      # SOLICITA QUE SEJA DIGITADO UM NUMERO PARA SER FATORADO
      # OU A LETRA "X" PARA ENCERRAR O PROCESSO
      num = input('\nInsira um número para ser fatorado ou "x" para sair: ')
      # SE FOI DIGITADO "X" ENCERRA O PROGRAMA
      if num == 'x':
        flag = False
        break
      # CASO CONTRARIO REALIZA A FATORACAO
      else:
        try:
          intNum = int(num)
          fatores = []
          # FATORANDO:
          # PARA CADA NUMERO PRIMO DA LISTA
          # ENTRA NO LOOP QUE VERIFICA SE A DIVISAO TEM RESTO
          # SE NAO TIVER ADICIONA O DIVISOR NA LISTA DE FATORES
          # ATUALIZA O NUMERO A SER DIVIDIDO E REPETE ATE QUE A DIVISAO SOBRE RESTO
          # QUANDO A DIVISAO SOBRA RESTO PULA PARA O PROXIMO NUMERO NA LISTA DE NUMEROS PRIMOS
          # E REINICIA O LOOP.
          # QUANDO O RESULTADO DA DIVISAO DO NUMERO A SER FATORADO PELOS NUMEROS PRIMOS DA LISTA
          # SOBRAR 1 ENCERRA O PROCESSO DE FATORACAO
          for f in (range(0, len(numPrimos))):
            while (intNum % numPrimos[f]) == 0:
              fatores.append(numPrimos[f])
              intNum //= numPrimos[f]
              if intNum == 1:
                break

          # IMPRIME NA TELA A LISTA COM O RESULTADO DAS DIVISOES
          print(f'FATORAÇÃO: {fatores}')
          
          # CONTRUINDO O RESULTADO:
          fatorado = []
          txtResp = ''

          # PERCORRE A LISTA "FATORES" ENQUANTO ESSA CONTIVER VALORES
          # A CADA ITERAÇÃO, ARMAZENA O VALOR DO FATOR EM UMA VARIÁVEL "FATOR"
          # E VERIFICA QUANTOS FATORES IGUAIS EXISTE NA LISTA
          # APLICANDO UM FILTRO, E ARMAZENANDO ESSES FATORES NUMA LISTA (FATORADO)
          # REALIZA A CONTAGEM DOS ELEMENTOS DA LISTA E ATUALIZA O TEXTO DA RESPOSTA
          # EM SEGUIDA ATUALIZA O CONTEUDO DA LISTA "FATORES" REMOVENDO OS ELEMENTOS JÁ CONTADOS.
          while(len(fatores)):
            fator = fatores[0]
            fatorado = [y for y in fatores if y == fator]
            if (len(fatorado) > 1):
              txtResp += str(fator) + '^' + str(len(fatorado)) + '.'
            else:
              txtResp += str(fator) + '.'
            fatores = [y for y in fatores if y != fator]
        
          # IMPRIME NA TELA O RESULTADO DA FATORAÇÃO
          print(f'O Número {num} fatorado é: {txtResp.rstrip(txtResp[-1])}')

        # O NÚMERO DIGITADO PARA FATORAÇÃO É INVÁLIDO
        # PERGUNTA SE QUER CONTINUAR E DE ACORDO COM A RESPOSTA, CONTINUA OU ENCERRA O PROGRAMA
        except:
          resp = ' '
          while (not resp in 'sSnN'):
            resp = input('Número inválido!\nDeseja continuar? [S/N]')
            if (resp in ('sS')):
              continue
            elif (resp in ('nN')):
              flag = False
      
    os.system('clear')
    print('Sistema encerrado...\nAté breve!')

  # O NÚMERO DIGITADO PARA A LISTA DE NÚMEROS PRIMOS É INVALIDO
  # PERGUNTA SE QUER CONTINUAR E DE ACORDO COM A RESPOSTA, CONTINUA OU ENCERRA O PROGRAMA
  except ValueError:
    resp = ' '
    while (not resp in 'sSnN'):
      resp = input('Número inválido!\nDeseja continuar? [S/N]')
      if (resp in ('sS')):
        continue
      elif (resp in ('nN')):
        flag = False