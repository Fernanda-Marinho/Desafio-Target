faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estado.values())

percentual = {estado: (valor/total) * 100 for estado, valor in faturamento_estado.items()}

print("percentual por estado:")
for e, p in percentual.items():
    print(f"{e}: {p:.2f}%")