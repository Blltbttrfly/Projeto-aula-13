temperatura = None
soma_temps = 0
contador_temperaturas = 0
media = 0
maior = None
menor = None
vezes = int(input("Digite quantas vezes voce quer checar sua temperatura: "))
historico = ""



for i in range(vezes):
    temperatura = float(input(f"Digite a temperatura {i+1}: "))
    historico += f"{i+1}. {temperatura} celsius"
    soma_temps += temperatura
    contador_temperaturas += 1 

    if maior == None:
        maior = temperatura
    
    if temperatura > maior:
        maior = temperatura
    
    if menor == None:
            menor = temperatura
    if temperatura < menor:
            menor = temperatura
    

media = soma_temps / contador_temperaturas

print(f"essa é sua media do dia: {media}")
print(f"A maior temperatura é {maior}")
print(f"A menor temperatura é {menor}")

