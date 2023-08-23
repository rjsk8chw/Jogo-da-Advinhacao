x = int(input('DIGITE UM NUMERO ENTRE 0 E 1024: '))
test = True
a = 0
b = 1024

if x == 0:
    print(f'O seu número é {x}. Obrigado por jogar!')
    test = False
elif x == 1024:
    print(f'O seu número é {x}. Obrigado por jogar!')
    test = False

while test:
    m = int((a + b) / 2)
    if x == m:
        print(f'....................'
              f'O seu número é'
              f'.....................'
              f' {m} !!!!!!!!!!!'
              f' Obrigado por jogar!')
        break
    elif x < m:
        b = m
    else:
        a = m
