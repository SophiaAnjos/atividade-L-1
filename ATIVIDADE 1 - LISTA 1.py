nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
nota4 = float(input("Digite a nota4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 4:
    situacao = "Em processo de Aprendizagem (Reprovado)"
elif media < 8:
    situacao = "Recuperação"
else:
    situacao = "Aprovado"

print("Situação do aluno:", situacao)