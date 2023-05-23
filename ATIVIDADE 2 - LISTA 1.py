tabela_precos = { 
    "Verde": "R$ 10,00",
    "Azul": "R$ 20,00",
    "Amarelo": "R$ 30,00",
    "Vermelho": "R$ 40,00"
}

cor = input("Digite a cor do seu jogo: ")

preco = tabela_precos.get(cor, "Cor inválida")

print("Preço:", preco)