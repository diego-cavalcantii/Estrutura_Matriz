'''
•	Escreva um programa que leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.
'''

matriz = []
maior_10 = 0

for lin in range(4):
    linha = []
    for col in range(4):
        linha.append(int(input(f"Linha {lin} - Digite um número  : ")))
    matriz.append(linha)

for lin in range(4):
    for col in range(4):
        if(matriz[lin][col] > 10):
            maior_10 += 1

print("\n==== Matriz ====")
for i in range(4):
    print(f"{matriz[i]}")

print(f"\n{maior_10} números maior que 10")
