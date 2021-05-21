# O programa irá calcular a nota de um aluno, especificando a variavel nome, variavel nota 1,2,3,4 ,
# variavel de soma dessas notas, variavel de media dessas notas. Uso de condicional simples, 
# para condicionar valor abaixo de 7 como reprovado. Uso de dicionario, 
# utilizando append para adicionar em lista de grupoAlunos.
# Ao final irá printar de forma a expor o calculo das notas, o nome do aluno e sua situação.


grupoAlunos = []
p = soma = 0

n_qtdade = int(input('Quantidade de alunos para saber as notas? '))    #Escreva um programa que leia os dados de N alunos 
print('')

for i in range (n_qtdade):
  aluno = {'nome':0, 'n1':0, 'n2':0, 'n3':0, 'n4':0, 'situacao':0} #dicionário

nomeAluno = str(input('Digite o nome do(a) aluno(a): '))       # nome string
n1 = float(input('Digite a 1ª nota que o(a) aluno(a) tirou: '))   # posso fixar as notas, sem precisar pergunta, comentando float em diante e substituindo por um valor de número inteiro.
n2 = float(input('Digite a 1ª nota que o(a) aluno(a) tirou: '))
n3 = float(input('Digite a 1ª nota que o(a) aluno(a) tirou: '))
n4 = float(input('Digite a 1ª nota que o(a) aluno(a) tirou: '))
somatorioNotas = (n1 + n2 + n3 + n4)
media = (somatorioNotas / 4)

if (media >= 7):
  resultado_final = ('Aprovado')
else:
  resultado_final = ('Reprovado')
    
 #dicionario proposto  e juntar concatenando com append para adicionar item ao final da lista
aluno['nomeAluno'] = nomeAluno
aluno['n1'] = n1
aluno['n2'] = n2
aluno['n3'] = n3
aluno['n4'] = n4
aluno['situacao'] = resultado_final
grupoAlunos.append(aluno)      

print('')
print('====> Nota(s) do(s) aluno(s): <====')
print('____' * 20)

#loop dos resultados que o programa irá me retornar

for aluno in grupoAlunos: 
  print('{}, as suas notas ({} + {} + {} + {}) = {} de somatorio ,\n divide por 4 para cálculo de média = {} de média,\n logo você esta {}.'
  .format(aluno['nomeAluno'], aluno['n1'],aluno['n2'], aluno['n3'], aluno['n4'],somatorioNotas, media, aluno['situacao']))