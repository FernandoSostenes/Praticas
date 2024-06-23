import random

num_secreto = random.randint(1,10)

print('Vamos jogar um jogo de adivinhação?! É bem simples, basta adivinhar um número entre 1 e 10, você possuirá 3 tentativas.\n')

palpites = 0

while palpites < 3:
    num = int(input('Porfavor, digite o palpite: '))
    palpites += 1

    if num != num_secreto:
        print(f'Número incorreto, tente novamente.\n')
    
    else:
        print('Acertou!')
        break

if num == num_secreto:
    print(f'Parabéns! O número secreto é {num_secreto} e vc acertos com {palpites} palpites\n')

else:
    print(f'Sinto muito, o numero de tentativas foi exedido, o número secreto era {num_secreto}, mais sorte na proxíma.')



