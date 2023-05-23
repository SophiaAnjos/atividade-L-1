dist = float(input("Digite a distância percorrida (em quilômetros): "))
comb = float(input("Digite a quantidade de combustível gasta (em litros): "))

cons_medio = dist / comb

g_combustivel = 4.50 * comb

print(f"Consumo médio: {cons_medio:.2f} km/l")
print(f"Gasto com combustível: R$ {g_combustivel:.2f}")