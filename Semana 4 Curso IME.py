# soma de sequencia de numeros usando while

pontos = int(input("Quantos valores deseja somar? "))
# determinar as variaveis
n = 0
soma = 0
valor = 1
# determinar o comando e ponto de parada do loop
while n != pontos:
    valor = int(input("Qual valor deseja somar: "))
    soma = soma + valor
    n = n + 1
print("Resultado:", soma,"\n")



# teste exercicios


## variaveis booleanas
## indicadores de passagem

decresc = True
valor = 1
anterior = int(input("digite o primeiro numero da sequencia: "))
while valor != 0 and decresc:
    valor = int(input("Digite o proximo da sequencia: "))
    if valor > anterior:
        decresc = False
    anterior = valor
if decresc:
    print("A sequencia esta em ordem decrescente\n")
else:
    print("nao acertou a ordem :(\n")

## indicadores de passagem para verificacao
print("\nCARTOES\n")
cardid = int(input("Digite o numero do cartao: "))
cardread = 1
foundcard = False

while cardread != 0 and not foundcard:
    cardread = (int(input("Digite o proximo cartao: ")))
    if cardread == cardid:
        foundcard = True
if foundcard:
    print("FOUND!")
else:
    print("NO NO NOT FOUND")


## n! (N FATORIAL exercise)

n = int(input("Digite o valor de n: "))
n_fat = n * (n-1)

print("n! = ",n_fat)
