# O programa irá receber um numero inteiro de 5 dígitos entre o valor determinado no exercício.
# Se o usuário digitar algo fora do parâmetro, o script irá ficar repetindo até ser colocado
#   um valor correto dentro do parâmetro.
#Utilização de função valida intervalo

def validar_dados(numero_digitado):
        try:
            n = int(n)
            if n >= 10000 and n < 30001:
                return ('Número correto, dentro do intervalo!')
            else:
                return ('Número incorreto, fora do intervalo!')
        except:
            return False


while True:
    print('Seja bem-vindo ao Cadastrador de Produto.\n')
    try:
        numero_digitado = int(input('Digite um numero entre 10000 e 30000: '))
    except:
        continue


    while validar_dados(numero_digitado):
        numero_string = str (numero_digitado)

    numero_cortado = list()
    for numero in numero_string:
        numero_cortado.append(numero)


    pesos = [2,3,4,5,6]
    resultado = list()


    for x in numero_cortado:
        resultado.append(int(x)*pesos[0])
        pesos.pop(0)
    resultado = sum(resultado) % 7
    print('Código do Produto: Código do Produto: {}-{}\n'.format(numero_digitado,resultado))
    break
    break