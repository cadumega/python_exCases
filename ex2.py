while True:
   num = int(input('Digite um número entre 10.000 e 30.000: '))

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

       print('{}-{}'. format(num,digito))

       break

print(a, b, c, d, e)
print(a1, a2, a3, a4, a5)
print(digito)
print(soma)
