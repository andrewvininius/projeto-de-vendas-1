# Criar um dicionário com informações sobre os produtos disponíveis
produtos = {
    "camisa": 50.0,
    "calça": 80.0,
    "jaqueta": 120.0,
    "meia": 10.0,
    "boné": 25.0
}

# Inicializar variáveis
total = 0.0
itens = []

# Loop principal
while True:
    # Mostrar os produtos disponíveis
    print("Produtos disponíveis:")
    for produto, preco in produtos.items():
        print(f"{produto} - R$ {preco:.2f}")

    # Perguntar ao cliente qual produto deseja comprar
    produto = input("Digite o nome do produto que deseja comprar ou pressione 'Enter' para sair: ")

    # Verificar se o cliente quer sair
    if not produto:
        break

    # Verificar se o produto está disponível
    if produto not in produtos:
        print("Produto não disponível")
        continue

    # Perguntar ao cliente quantos itens deseja comprar
    quantidade = int(input("Digite a quantidade que deseja comprar: "))

    # Calcular o preço total do item e adicioná-lo ao total da compra
    preco_item = produtos[produto] * quantidade
    total += preco_item

    # Adicionar o item à lista de itens comprados
    itens.append(f"{quantidade}x {produto} - R$ {preco_item:.2f}")

# Mostrar a lista de itens comprados e o total da compra
if itens:
    print("Itens comprados:")
    for item in itens:
        print(item)
    print(f"Total da compra: R$ {total:.2f}")
else:
    print("Nenhum item comprado.")


