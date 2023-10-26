'''
•	Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.
'''

matriz = []
lista_maior = []

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(int(input(f"Linha {lin} - Digite um número inteiro : ")))
    matriz.append(linha)

maior_soma = sum(matriz[0])

for i in range(len(matriz)):
    soma = sum(matriz[i])
    if (soma > maior_soma):
        maior_soma = soma
        lista_maior.append(matriz[i])

print("\n==== Matriz ====")
for i in range(len(matriz)):
    print(f"{matriz[i]}")

print("")
print(f"Linha de maior soma \n{lista_maior} = {maior_soma}")




