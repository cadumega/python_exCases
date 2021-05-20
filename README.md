# python_exCases
 Exercises to solve, with python and programming logic.

 Para que você ganhe nota máxima em cada exercício, você precisará cumprir os três requisitos básicos explicados nas ORIENTAÇÕES GERAIS: 

• Apresentar seu algoritmo completo, indentado e organizado;

• Explicar seu código através de comentários; 

• Colocar uma IMAGEM com o terminal rodando e mostrando o que cada exercício pede. 

_____________________________

ok Exercício 1: 
Escreva um programa que leia o nome de um lutador e seu peso. 


Em seguida, informe a categoria a que pertence o lutador, conforme a Tabela a seguir (note que a tabela foi criada para efeito deste exercício e não condiz com qualquer categoria de luta). 

A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir:

No modelo de relatório da disciplina você encontrará um exemplo de exercício para um melhor entendimento. 
Caso você desenvolva seu código corretamente e funcional, porém não faça os comentários nem coloque uma imagem dele funcionando no terminal, terá sua nota severamente prejudicada.

Resolva os algoritmos abaixo em Python seguindo todas as instruções listadas neste documento. 

Exercício 1: Escreva um programa que leia o nome de um lutador e seu peso. 
Em seguida, informe a categoria a que pertence o lutador, conforme a Tabela a seguir (note que a tabela foi criada para efeito deste exercício e não condiz com qualquer categoria de luta). 

A saída do programa deve exibir na tela uma frase com o padrão descrito a seguir:

Nome fornecido: Pepe Jordão 
Peso fornecido: 73.4  

Frase a ser exibida: O lutador Pepe Jordão pesa 73,4 kg e se enquadra na categoria Ligeiro



Todos os dados devem ser lidos do teclado, sendo que o nome do lutador é uma string e o peso é um número real. Não é necessário armazenar os dados em uma estrutura de dados, basta imprimir na tela.

Coloque todo o seu programa dentro de um laço de repetição e faça-o se encerrar quando uma determinada condição for satisfeita. A condição fica a seu critério, como por exemplo, encerrar o programa ao digitar a palavra sair, ou então um peso inválido como o valor zero.

Exemplo de um programa que lê o nome de um lutador e seu peso:

nome = str(input('nome do lutador'))  

peso = float(input('peso do lutador'))    

# categoria = float(input(' categoria pertencente ao lutador'))  

if peso < 65:

   print('O lutador',nome,' pesa ',peso,' kg e se enquadra na categoria pena')

else:

   if peso >= 65 and peso < 72:

       print('O lutador ',nome,' pesa ',peso,' kg)

   else:

       if peso >= 72 and peso < 79:

           print('O lutador ',nome,' pesa ',peso,' kg )

Lembre-se de que na linguagem python, existe a obrigatoriedade do uso de endentação,  uma  vez que em outras linguagens de programação não é obrigatório , apenas uma maneira de organizar tudo.

Além disso na linguagem python, quando termina a endentação, também finaliza a visualização do bloco de instruções,  quando todos os comandos passam a ser escritos com letras minúsculas e em inglês.

__
Um programa que leia o nome de um lutador e o seu peso pode ser desenvolvido da seguinte maneira:
nome = str(input('nome do lutador'))  
peso = float(input('peso do lutador'))    
# categoria = float(input(' categoria pertencente ao lutador'))  
if peso < 65:
  print('O lutador',nome,' pesa ',peso,' kg e se enquadra na categoria pena')
else:
  if peso >= 65 and peso < 72:
      print('O lutador ',nome,' pesa ',peso,' kg)
  else:
      if peso >= 72 and peso < 79:
          print('O lutador ',nome,' pesa ',peso,' kg)





_____________

Exercício 2: 
Escreva um programa que receba como parâmetro de entrada um número inteiro de 5 dígitos no intervalo fechado [10000, 30000] que represente códigos de produtos vendidos em uma loja. 

Crie uma função para validar os dados de entrada, obrigando o usuário a respeitar o intervalo e o tipo de dado (inteiro). Crie mais uma função que calcule e retorne o dígito verificador do código, utilizando a regra de cálculo explicada a seguir. 

Por exemplo, considere o código 21853, em que cada dígito é multiplicado por um peso começando em 2, os valores obtidos são somados, e do total obtido calcula-se o resto de sua divisão por 7.



Retorne na função o valor do dígito verificador calculado e imprima na tela o código do produto digitado e seu dígito verificador separado por hífen, como: 21853-5. 

Imprima na tela um teste do seu programa utilizando como código os 5 primeiros dígitos do seu RU. Se seu RU tiver menos de 5 dígitos, complete com zeros. Se seu RU cair fora do intervalo especificado, realize o teste mesmo assim. 


Dica do Professor: você precisará dividir o valor do código a ser verificado, que será um inteiro, em partes que podem ser manipuladas individualmente. 

Uma das possíveis maneira de fazer isso é converter o valor inteiro para uma lista e manipular os índices da lista individualmente. Usar listas é somente uma possibilidade, e não a única. Você consegue solucionar o exercício também sem listas, somente com cálculos matemáticos. Use o raciocínio e a pesquisa para encontrar soluções! 

https://www.guj.com.br/t/exercicio-em-python/415176
Explicação:

cheguei até aqui batendo cabeça

# exercicio2

while True:

   num = int(input('Digite um número entre 10000 e 30000: '))

   if num < 10000:

       continue

   if num > 30000:

       continue

   else:

       a = num // 1 % 10

       b = num // 10 % 10

       c = num // 100 % 10

       d = num // 1000 % 10

       e = num // 10000 % 10

       a1 = (a * 6)

       a2 = (b * 5)

       a3 = (c * 4)

       a4 = (d * 3)

       a5 = (e * 2)

       soma = a1 + a2 + a3 + a4 + a5

       digito = soma % 7

       print('{}-{}'.format(num,digito))

       break

print(a, b, c, d, e)

print(a1, a2, a3, a4, a5)

print(digito)

print(soma)

____


_________
Exercício 3: 
Considere o seguinte conjunto de dados: Nome + [N1, N2, N3, N4] + Status, que deve ser colocado em um dicionário. 

O nome representa o nome de um aluno e deve ser usado como chave. Já N1, N2, N3, N4 representam as notas de provas desse aluno e são armazenadas em uma lista. Por fim, o status nada mais é do que uma string contendo a palavra Aprovado ou Reprovado. 
Utilize uma estrutura de dicionário com listas para resolver este exercício. 

Escreva um programa que leia os dados de N alunos e apresente na tela se foram aprovados ou reprovados. O critério que garante a aprovação é que a média aritmética das 4 notas seja maior ou igual 7,0. 

O valor de N é a quantidade de alunos, e esse valor deve ser lido do teclado no começo do programa. Faça um laço de repetição para a leitura destes N alunos. As notas devem ser exibidas ao final do programa com uma casa decimal de precisão.



Imprima na tela um teste do seu programa usando como primeiro cadastro o seu nome, e como nota os 4 primeiros dígitos do seu RU. Dica do Professor: crie um dicionário no formato: alunos = {'nome':[], 'notas':[], 'status':[]}


No enunciado é bem claro que o nome do aluno deve servir como chave do dicionário: "Nome representa o nome de um aluno e deve ser usado como chave", mas você definiu duas chaves, Aluno e Notas.

Então, basicamente falta seguir o que o enunciado pede:

N = int(input('Quantos alunos? '))

students = {}

for i in range(1, N+1):
  name = input(f'Nome do aluno {i}: ')
  grades = []

  for j in range(1, 5):
    grade = float(input(f'Nota {j} do aluno {i}: '))
    grades.append(grade)

  students[name] = grades

for name, grades in students.items():
  average = sum(grades) / len(grades)
  result = 'aprovado' if average >= 7.0 else 'reprovado'
  print(f'O aluno {name} foi {result} com média {average:.1f}')






__________

Exercício 4: 
Crie um programa que contenha três listas para ler e armazenar o nome, a idade e o número do telefone de seus contatos telefônicos. Ao digitar uma string vazia para o nome, o programa interrompe a leitura e se encerra. 


Apresente na tela os dados cadastrados em ordem alfabética pelo nome dos contatos. Uma possível solução de ordenar alfabeticamente é usar o método sort. 


Em seguida, armazene os contatos em outros dois dicionários, utilizando como critério a idade: menores de 18 anos em um e os maiores em outro dicionário, eliminando o original. Apresente na tela os dois dicionários resultantes da separação. Utilize como chave dos dicionários: nome, idade e telefone. 


Imprima na tela um teste do seu programa usando como primeiro cadastro o seu nome, como telefone o seu RU, e como idade os dois últimos dígitos do seu RU. 



Dica do Professor: você precisará criar inicialmente no seu programa três listas (nomes, idades e telefones). Ao realizar a ordenação, você irá ordenar somente a lista de nomes, mas ao realizar a impressão na tela, não esqueça que deve imprimir todos os dados do contato juntos do nome.

Note também que para a última parte do exercício as listas deverão se transformar em um dicionário contendo os cadastros.


