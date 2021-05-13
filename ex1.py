#variáveis nome e peso , uso de ponto para número float

print('''Pesquisa Lutador/Categoria
[1] RESPONDER
[2] SAIR ''')
print()
opcao = int(input('Escolha a sua opçao 1 ou 2? '))

if opcao==1:
  nome = str(input('Qual o nome do lutador? '))  
  peso = float(input('Qual o peso do lutador em kg? '))    

#categoria

  if peso < 65:
    print('O lutador {}, pesa {}kg e esta na categoria Pena.'. format(nome,peso))
  elif peso >= 65 and  peso <= 72:
    print('O lutador {}, pesa {}kg e esta na categoria Leve.'. format(nome,peso))
  elif peso >= 72 and peso <= 79:
    print('O lutador {}, pesa {}kg e esta na categoria Ligeiro.'. format(nome,peso))
  elif peso >= 79 and peso <= 86:
    print('O lutador {}, pesa {}kg e esta na categoria Meio-médio.'. format(nome,peso))
  elif peso >= 86 and peso <= 93:
    print('O lutador {}, pesa {}kg e esta na categoria Médio.'. format(nome,peso))
  elif peso >= 93 and peso <= 100:
    print('O lutador {}, pesa {}kg e esta na categoria Meio-pesado.'. format(nome,peso))
  elif peso >= 100 and peso <=318:
    print('O lutador {}, pesa {}kg e esta na categoria Pesado.'. format(nome,peso))
  elif peso <= 50 and peso >= 318:
    print('Peso {} inválido.'. format(peso))

  print('=== Fim da Pesquisa ===')

if opcao==2:
  print('=== Fim da Pesquisa ===')




# print('O lutador {}, pesa {} kg e se enquadra na categoria {}.'. format(nome,peso,categoria))
