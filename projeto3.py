'''
•	Faça um programa que leia uma matriz 6x3 com números reais, calcule e mostre:
(a) o maior elemento da matriz e sua respectiva posição (linha e coluna);
(b) o menor elemento da matriz e sua respectiva posição.
'''

matriz = []

for lin in range(6):
    linha = []
    for col in range(3):
        linha.append(float(input(f"Linha {lin} - Digite um número real : ")))
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]

for lin in range(6):
    for col in range(3):
        if(matriz[lin][col] > maior):
            maior = matriz[lin][col]
            linha_maior = lin
            col_maior = col
        if(matriz[lin][col] < menor):
            menor = matriz[lin][col]
            linha_menor = lin
            col_menor = col

print("\n==== Matriz ====")
for i in range(len(matriz)):
    print(f"{matriz[i]}")

print(f"\nMaior número = {maior} - Linha = {linha_maior} - Coluna = {col_maior}")
print(f"Menor número = {menor} - Linha = {linha_menor} - Coluna = {col_menor}")



