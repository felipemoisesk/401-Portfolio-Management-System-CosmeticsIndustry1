i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()

while i == 'S':
    print('\n[1] Atualizar BP BR\n'
          '[2] Atualizar PM LT\n'
          '[3] Atualizar VG FULL\n'
          )

    x = int(input('Qual dataset você deseja atualizar?\nDigite o número: '))
    if x == 1:
        print('BLOCO1')
        i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
    elif x == 2:
        print('BLOCO2')
        i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
    else:
        print('BLOCO3')
        i = input('Você deseja atualizar algum dataset?\nDigite [S] ou [N]: ').upper()
print('FIM')
