import os

os.system('clear')

print('##### CONVERSOR DECIMAL PARA BINÁRIO E HEXADECIMAL #####\n')

flag = ''

while(True):
  print('Digite um número [\'q\' para sair]:\n')
  flag = input()
  if flag == 'q' or flag == 'Q':
    break
  else:
    try:

      # CONVERTER PARA BINÁRIO
      t = int(flag)
      r = 0
      b = '0' if t == 0 else '' 
      while(t > 0):
        r = 1 if (t % 2) else 0
        t //= 2
        b += str(r)

      # CONVERTER PARA HEXADECIMAL
      baseHex = {
                  10 : 'A',
                  11 : 'B',
                  12 : 'C',
                  13 : 'D',
                  14 : 'E',
                  15 : 'F'
                }
      
      t = int(flag)
      i = 0
      r = 0
      h = '0' if t == 0 else '' 
      while(t > 0):
        i = t // 16
        r = int((t / 16 - i) * 16)
        t //= 16
        if (r > 9):
          r = baseHex.get(r)
        h += str(r)

      print('\n' + '::::BINÁRIO: ' + b[::-1])
      print('HEXADECIMAL: ' + h[::-1] + '\n\n')

    except ValueError:
      print('Você digitou um número inválido!')
    
os.system('clear')
print('Aplicação finalizada!\nAté breve!')