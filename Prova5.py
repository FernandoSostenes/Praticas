print('----MÉDIA DE NOTAS DOS ALUNOS DA DISCIPLINA----')

num_alunos = int(input('Porfavor digite o número de alunos: '))

for _ in range(num_alunos):
    nome_aluno = input(f'\nDigite o nome do Aluno {_+1}: ')
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    nota_3 = float(input('Digite a terceira nota: '))

    media_notas = (nota_1 + nota_2 + nota_3)/3

    if (media_notas) >= 7:
        situacao = 'Aprovado'

    else:
        situacao = 'Reprovado'

    print(f'\nO aluno {nome_aluno} com as notas {nota_1, nota_2, nota_3} foi {situacao} com média {media_notas:.2f}.')

print('\n----FIM DO PROGRAMA----')