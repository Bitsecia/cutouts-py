import os
flag = True

while (flag):
  numPrimos = []
  os.system('clear')
  count = input('Digite a quantidade de números primos que você quer testar: ')
  
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

    print(f'\nNumeros Primos encontrados: {numPrimos}')

    # PROCESSO DE FATORAÇÃO:
    while (flag):
      num = input('\nAgora insira um número para ser fatorado: ')

      try:
        intNum = int(num)
        fatores = []
        # FATORANDO
        for f in (range(0, len(numPrimos))):
          while (intNum % numPrimos[f]) == 0:
            fatores.append(numPrimos[f])
            intNum //= numPrimos[f]
            if intNum == 1:
              break

        print(f'FATORAÇÃO: {fatores}')
        
        # CONTANDO
        fatorado = []
        for fator in fatores:
          exp = 0
          strFator = str(fator)
          for x in range(0, len(fatores)):
            if (fator == fatores[x]):
              exp += 1
              del(fatores[x])
            # fatores.remove(fator)
            fatorado.append(str(fator) + '^' + str(exp))
        
        print(f'O Número {num} fatorado é: {fatorado}')

      except:
        resp = ' '
        while (not resp in 'sSnN'):
          resp = input('Número inválido!\nDeseja continuar? [S/N]')
          if (resp in ('sS')):
            continue
          elif (resp in ('nN')):
            flag = False
      

  except ValueError:
    resp = ' '
    while (not resp in 'sSnN'):
      resp = input('Número inválido!\nDeseja continuar? [S/N]')
      if (resp in ('sS')):
        continue
      elif (resp in ('nN')):
        flag = False