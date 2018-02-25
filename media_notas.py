#Calcular a média de 5 notas

notas = [6.5, 7.5, 3.4, 8.9, 5.4]

soma_notas = 0;

for x in range(1, len(notas)):
    soma_notas += notas[x]

media = soma_notas/len(notas)

print("A media das notas é igual a %.2f" %media)