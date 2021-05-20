#variáveis nome e peso , uso de ponto para número float

# O programa foi criado para especificar o nome , o peso e a categoria que um lutador se encaixa.
# Tendo um laço de repetição caso o usuário da pesquisa queira continuar respondendo respondendo 'sim' ou 's', 
# otimizar depois colocando uma condição de desfecho se não quiser mais responder o questionário.
# Tentei deixar mais humano, como um aplicativo de cadastro ou respostas mais humanizadas.

repetirPesquisa = 'S' or 's' or 'sim' or 'Sim'
while repetirPesquisa == 'S' or repetirPesquisa == 's' or repetirPesquisa == 'Sim' or repetirPesquisa == 'sim':
    print(' ')
    print('=== Olá, esteja pronto para as perguntas abaixo. ===')
    print(' ')
    nome = str(input('Qual o nome do lutador? '))  
    peso = float(input('Qual o peso do lutador em kg? '))    

  #categoria
    if peso < 65:
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Pena.'. format(nome,peso))
    elif peso >= 65 and  peso <= 72:
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Leve.'. format(nome,peso))
    elif peso >= 72 and peso <= 79:
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Ligeiro.'. format(nome,peso))
    elif peso >= 79 and peso <= 86:
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Meio-médio.'. format(nome,peso))
    elif peso >= 86 and peso <= 93:
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Médio.'. format(nome,peso))
    elif peso >= 93 and peso <= 100:
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Meio-pesado.'. format(nome,peso))
    elif (peso >= 100):
      print('O lutador {}, pesa {:.1f}kg e esta inserido na categoria Pesado.'. format(nome,peso))
    else: 
      print('Peso {:.1f} inválido.'. format(peso))

    print(' ')
    print("=== Agradecemos a sua resposta. ===")
    print(' ')
    repetirPesquisa = input('Deseja repetir a pesquisa? [S/N] ')




# print('O lutador {}, pesa {} kg e se enquadra na categoria {}.'. format(nome,peso,categoria))

  # print('''Pesquisa Lutador/Categoria
  # [1] RESPONDER
  # [2] SAIR ''')
  # print()
  # opcao = int(input('Escolha a sua opcao 1 ou 2? '))