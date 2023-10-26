'''
•	Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação .
'''

matriz = []

for lin in range(3):
    linha = []
    for col in range(3):
        linha.append(int(input(f"Linha {lin} - Digite um número inteiro : ")))
    matriz.append(linha)

print("\n==== Matriz ====")
for i in range(len(matriz)):
    print(f"{matriz[i]}")

num = int(input("\nDigite um número para multiplicar a diagonal principal : "))


matriz[0][0] *= num
matriz[1][1] *= num
matriz[2][2] *= num

print("\n==== Matriz ====")
for i in range(len(matriz)):
    print(f"{matriz[i]}")