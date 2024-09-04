import json 

def pegar_vetor(f):
    with open(f, 'r') as file:
        data = json.load(file)
    
    faturamento = [dia["valor"] for dia in data if dia["valor"] > 0]

    return faturamento

def calculos_faturamento(v):

    menor = min(v)
    maior = max(v)
    media = sum(v) / len(v)
    dias_acima_media = len([valor for valor in v if valor > media])

    return menor, maior, dias_acima_media

vetor = pegar_vetor('dados.json')

menor, maior, dias_acima = calculos_faturamento(vetor)

print(f"menor: R$ {menor:.2f}")
print(f"maior: R$ {maior:.2f}")
print(f"dias acima da media: {dias_acima}")
