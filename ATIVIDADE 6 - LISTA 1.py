cod = int(input("Digite o código do operário: "))
h_trab = float(input("Digite o número de horas trabalhadas: "))

sal = h_trab * 10.00

if h_trab > 50:
    h_ex = h_trab - 50
    pag_ex = h_ex * 20.00
else:
    h_ex = 0
    pag_ex = 0

print("Salário total:", sal)
print("Salário excedente:", pag_ex)