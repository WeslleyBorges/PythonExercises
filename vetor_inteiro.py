vetor_inteiro = [];

for x in range(0,5):
    vetor_inteiro.append(int(input('Insira um número na posição ' + str(x) + ' do vetor: ')))

print('\n')

for x in range(0,len(vetor_inteiro)):
    print('Posição {0}: {1}' .format(x, vetor_inteiro[x]))