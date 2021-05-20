grupoAlunos = []
p = soma = 0


for i in range (n):
  aluno = {'nome':0, 'n1':0, 'n2':0, 'n3':0, 'n4':0, 'situacao':0} #dicionário

nome = input('Digite o nome do(a) aluno(a): ')
  n1 = float(input('Digite a 1ª nota do(a) aluno(a): '))
  n2 = float(input('Digite a 2ª nota do(a) aluno(a): '))
  n3 = float(input('Digite a 3ª nota do(a) aluno(a): '))
  n4 = float(input('Digite a 4ª nota do(a) aluno(a): '))
  soma_notas = (n1 + n2 + n3 + n4)
  media = (soma_notas / 4)
  
  if (media >= 7):
    resultado_final = ('Aprovado')
  else:
    resultado_final = ('Reprovado')
    
 #preenchimento do dicionário
    aluno['nome'] = nome
    aluno['n1'] = n1
    aluno['n2'] = n2
    aluno['n3'] = n3
    aluno['n4'] = n4
    aluno['situacao'] = resultado_final
    lista_de_alunos.append(aluno)#concatenei a lista com os dados dos alunos

  print('')
  print('Notas dos alunos')
  print('- ' * 10)

#loop dos resultados que o programa irá me retornar

  for aluno in lista_de_alunos: 
    print('{} {} {} {} {} {} {}'.format(aluno['nome'], aluno['n1'],aluno['n2'], aluno['n3'], aluno['n4'],
    media, aluno['situacao']))




























while True:

  try:
    print('---' * 10)
    nome = input('Nome do aluno: ').strip().capitalize()
    n1 = float(input('1a Nota: '))
    n2 = float(input('2a Nota: '))
    n3 = float(input('3a Nota: '))
    n4 = float(input('4a Nota: '))

    alunos[nome] = ([n1, n2, n3, n4])
    des = input('Deseja continuar? [S/N]: ').upper().strip()[0]

    if des == 'N':
       break
  except:
    print('Dado inválido!')
    
  for i, j in alunos.items():
      soma = j[p] + j[p+1] + j[p+2] + j[p+3]
      
      if soma / 4 >= 7:
          print(f'{i}: {j[p]} {j[p+1]} {j[p+2]} {j[p+3]} Média: {soma/ 4:.1f} APROVADO!!!')
      else:
          print(f'{i}: {j[p]} {j[p + 1]} {j[p + 2]} {j[p+3]} Média:{soma / 4:.1f} REPROVADO :(')