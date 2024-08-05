primeiro = int(input('Digite o primeiro numero de seu intervalo: '))
ultimo = int(input('Digite o ultimo numero de seu intervalo: '))

soma_pares = 0

for numero in range(primeiro,ultimo+1):
    if numero % 2 == 0:
        soma_pares += numero


if soma_pares == 0:
    print("Nao ha numeros pares no intervalo fornecido.") 

else:
    print(f"A soma dos numeros pares no intervalo é: {soma_pares}")

