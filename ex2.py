# # O programa irá receber um numero inteiro de 5 dígitos entre o valor determinado no exercício.
# # Utilizar RU conforme o exercício solicitado.
# # Comentei a linha de exemplo, se fosse o usuário digitar algo fora da faixa de valores, 
#       o script irá ficar repetindo até ser colocado,
# #         um valor correto dentro da faixa!! já que esta com laço while.
# #Utilização de variável ru_faixa para validar intervalo

while True:

   ru_faixa = 25570            #int(input('Digite um número entre 10000 e 30000, use o seu RU: '))
   if ru_faixa < 10000:
     print('Valor fora da faixa, tente novamente e digite um número com 5 dígitos maior que 10000 ou menor que 30000.')
     print('')
     continue

   elif ru_faixa > 30000:
     print('Valor fora da faixa, tente novamente e digite um número com 5 dígitos maior que 10000 ou menor que 30000.')
     print('')
     continue
    

   else:
     a = ru_faixa // 1 % 10
     b = ru_faixa // 10 % 10
     c = ru_faixa // 100 % 10
     d = ru_faixa // 1000 % 10
     e = ru_faixa // 10000 % 10

#PESO
     a1 = (a * 6)
     a2 = (b * 5)
     a3 = (c * 4)
     a4 = (d * 3)
     a5 = (e * 2)

     somatorio = a1 + a2 + a3 + a4 + a5
     resto = somatorio % 7

     print('{}-{}'.format(ru_faixa,resto))   #imprima na tela o código digitado e seu dígito verificador por hífen

     break

print(a, b, c, d, e)
print(a1, a2, a3, a4, a5)
print(resto)
print(somatorio)
