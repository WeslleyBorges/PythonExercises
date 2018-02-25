vetor = []

for x in range(0, 10):
    vetor.append(int(input('Insira um número na posição {0}: ' .format(x))))

print()
print('Vetor invertido: ')

print('Posição por posição: ')
for x in range(len(vetor) - 1, -1, -1):
    print(vetor[x])

print('De rabo a cabo: ')
print(vetor.reverse())