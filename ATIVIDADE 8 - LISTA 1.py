n = int(input("Digite um número inteiro: "))

primo = True
if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
else:
    primo = False

if primo:
    print(n, "é primo.")
else:
    print(n, "não é primo.")