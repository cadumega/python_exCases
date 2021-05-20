dicionario_aux = dict()
maiores_18 = dict()
menores_18 = dict()
print("Bem-Vindo ao Cadastrador de Contatos! ")

while True:
    nome = input("Digite seu nome: ")

    if nome.startswith(" ") or nome=="":
        break
 
    idade = int(input("Digite sua Idade: "))
    quantos_numeros = int(input("Quantos números de contato você gostaria de adicionar? "))
    telefones_de_contato = list()
 
    while len(telefones_de_contato)<quantos_numeros: 
        numero = input("Cadastre 1 Numero: ")
        telefones_de_contato.append(numero)
        dicionario_aux[nome] = {"idade": idade,"contatos": telefones_de_contato}

    for chave,valor in dicionario_aux.items():
        contatos = valor.get('contatos')
        idade = valor.get('idade')
        if idade <18:
            menores_18[chave] = {"contatos":contatos,"idade": idade }
    else:
            maiores_18[chave] = {"contatos":contatos,"idade": idade }


novo_list = sorted(dicionario_aux.items())
contador = 0

for x in novo_list:#fará a contagem de quantos registros tem.
    contador += 1
    print("\n")
    print("========= DADOS DO REGISTRO Nº {} ==========".format(contador))

    print("Nome do contato: ",x[0])
    print("Idade do Contato: " ,x[1].get('idade'))
    print("Telefones de Contato:", x[1].get('contatos')[0])
    print("=========================================")
    print("\n")

dicionario_aux = {}
menor_idade_list = sorted(menores_18.items())
contador = 0
print("-------- MENOR DE IDADE -------")


for x in menor_idade_list:
    print('\n')
    print("Nome do contato: ",x[0] )
    print("Idade do Contato: " ,x[1].get('idade'))
    print("Telefones de Contato:", x[1].get('contatos')[0])
    print("=========================================")
    print("\n")
maior_idade_list = sorted(maiores_18.items())
contador = 0
print("------- MAIOR DE IDADE -------")


for x in maior_idade_list:
    contador += 1
    print('\n')
    print("Nome do contato: ",x[0] )
    print("Idade do Contato: " ,x[1].get('idade'))
    print("Telefones de Contato:", x[1].get('contatos')[0]) print("=========================================")
    print("\n")