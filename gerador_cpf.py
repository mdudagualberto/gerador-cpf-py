import random
import sys

cpf_teste_1= ''
for i in range(9):
    cpf_teste_1 += str(random.randint(0, 9))

lista = []
indice= 10
for digito in cpf_teste_1:
    digito_int= int(digito)
    multiplicacao= digito_int * indice
    lista.append(multiplicacao)
    indice -= 1

soma= 0
for i in lista:
    soma += i

nova_soma = soma * 10
resto = nova_soma % 11

if resto > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto


cpf_teste_2= cpf_teste_1 + str(primeiro_digito)

resultado = 0
contador = 11

for digito in cpf_teste_2:
    resultado += int(digito) * contador
    contador -= 1

novo_resultado = (resultado * 10) % 11
if novo_resultado > 9:
    novo_resultado = 0
else:
    novo_resultado = novo_resultado

cpf_gerado= cpf_teste_1 + str(primeiro_digito) + str(novo_resultado)
print(cpf_gerado)




sys.exit()