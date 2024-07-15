listaprodutos = []
carrinho = []
estoque = {
    "Bebidas": {"Monster": 10, "Bela Roma": 8, "Skol": 2.50, "Coca Cola": 9 },
    "Bolachas": {"Negresco": 2.75, "Choconegro": 2.00, "Oreo": 3.50},
    "Alimentos": {"Miojo": 2.50, "Ovo 12un": 12, "Ovo 20un": 20, "Arroz 5kg": 30, },
}

    # keys ^
while True:
    print("\n" * 50)
    print('[1] entrar como cliente')
    print('[2] entrar como funcionario')
    print('[3] cadastro')

    resposta = input(": ")
    acabar = False

    if resposta == "1":
        while acabar == False:
            print("\n" * 50) # limpar a tela
            print("Entrou como cliente! selecione a opção desejada. \n")
            print("[1] Comprar")
            print("[2] Ver carrinho")
            print("[3] Finalizar compra")
        
            resposta = input(": ")
            if resposta == "1": # opção 1 comprar
                print("\n" * 50)
                print("Selecione a categoria: \n")
        
                for i in estoque.keys():
                    print(i)
                categoria = input(": ")
        
                print("\n" * 50)
                print("Selecione os produtos, 0 para voltar: \n")
                for item, valor in estoque[categoria].items():
                    print(item, valor, "R$")
        
                while True:
                    produto = input(": ")
                    if produto in estoque[categoria]:
                        carrinho.append(estoque[categoria][produto])
                        listaprodutos.append(produto)
                        print("Produto adicionado com sucesso")
                    elif produto == "0":
                        break

            elif resposta == "2": # opção 2 carrinho
                while True:
                    print("\n" * 50)
                    print("0 para voltar, 1 para remover item")
                    print("Carrinho: \n")

                    for idx, (item, valor) in enumerate(zip(listaprodutos, carrinho), start=1):
                        print(f"{idx}. {item}: {valor} R$")
                    print(f"Total: {sum(carrinho)}R$")

                    opcao = input(": ")
                    if opcao == "1":
                        while True:
                            idx_remover = int(input("Digite o número do item que deseja remover: "))
                            if 1 <= idx_remover <= len(carrinho):
                                item_removido = listaprodutos.pop(idx_remover - 1)
                                valor_removido = carrinho.pop(idx_remover - 1)
                                break
                    elif opcao == "0":
                        break

            elif resposta ==  "3": # opção 3 finalizar compra
                while True:
                    print("\n" * 50)
                    print("Selecione a forma de pagamento:")
                    print("[1] Dinheiro")
                    print("[2] Pix")
                    print("[3] Cartão Debito")
                    print("[4] Cartão Crédito")
                    pagamento = input(": ")

                    if pagamento == "1":
                        print("Digite o valor que esta sendo entregue")
                        valor = float(input(": "))

                        if valor > sum(carrinho): # compra foi aprovada
                            print("\n" * 50)
                            print(f"Troco: {round(valor - sum(carrinho), 2)}R$")
                            acabar = True
                            break
                        elif valor < sum(carrinho):
                            print("Compra não autorizada, utilize outra forma de pagamento")
                            x = input("Digite qualquer tecla para voltar: ")
                        else:
                            print("\n" * 50)
                            acabar = True
                            break

                    elif pagamento == "2" or pagamento == "3" or pagamento == "4":
                        print("Informe o saldo existente na conta: ")
                        saldo = float(input(": "))

                        if saldo >= sum(carrinho): # compra foi aprovada
                            print("\n" * 50)
                            acabar = True
                            break
                        elif saldo < sum(carrinho):
                            print("Compra não autorizada, utilize outra forma de pagamento")
                            x = input("Digite qualquer tecla para voltar: ")
        else: # saiu de todos os whiles, código da nota fiscal aqui
            print("Compra aprovada!")
            print("\n---= nota fiscal =---")
            print("\n")

            for idx, (item, valor) in enumerate(zip(listaprodutos, carrinho), start=1):
                    print(f"{idx}. {item}: {valor} R$")
            print("\n")
            print(f"Total sem impostos: {sum(carrinho)}R$")

            # impostos
            valor = sum(carrinho)

            Lnacional = valor * 0.05
            valor = valor + Lnacional

            Lestadual = valor * 0.08
            valor = valor + Lnacional

            Lmunicipal = valor * 0.12
            valor = valor + Lnacional

            print(f"Total com impostos: {round(valor, 2)}R$")
            print("\n")
            print(f"Pago em imposto nacional: {round(Lnacional, 2)}R$")
            print(f"Pago em imposto estadual: {round(Lestadual, 2)}R$")
            print(f"Pago em imposto municipal: {round(Lmunicipal, 2)}R$")
            x = input("")


#####################################################


    elif resposta == "2": # entrar como funcionario
        try:
            print("\n" * 50)
            print("---= Faça login para entrar =---\n")
            loginnome = input("nome: ")
            logincpf = input("cpf: ")

            if loginnome == nome and logincpf == cpf:
                while True:
                    print("\n" * 50)
                    print("Login autorizado com sucesso")
                    print("Escolha a opção: \n")
                    print("[0] voltar")
                    print("[1] consultar estoque")
                    print("[2] atualizar estoque")
                    print("[3] adicionar produtos")
                    res = input(": ")

                    if res == "0":
                        break

                    elif res == "1":
                        print("\n" * 50)
                        print('---= Estoque =---\n')

                        print("Categorias: ")
                        print("\n")
                        for i in estoque.keys():
                            print(i)
                        
                        print("\n")

                        print("Produtos: ")
                        for categoria, produtos in estoque.items():
                            print(f"Categoria: {categoria}")
                            for produto in produtos.keys():
                                print(f" - {produto}")

                        x = input("Digite qualquer tecla para voltar: ")

                    elif res == "2": # atualizar estoque
                        while True:
                            print("\n" * 50)
                            print('---= Atualizar Estoque =---\n')
                            print("[0] Voltar")
                            print("[1] Modificar preço")
                            print("[2] Remover produto")
                            print("[3] Remover categoria")
                            opcao = input(": ")

                            if opcao == "1":
                                print("\n" * 50)
                                print('---= Modificar Preço =---\n')
                                print("Selecione a categoria do produto\n")
                                for i in estoque.keys():
                                    print(i)

                                categoria = input(": ")
                                print("\n")

                                for item, valor in estoque[categoria].items():
                                    print(item, valor, "R$")

                                print("Digite o item que quer modificar")
                                modificar = input(": ")

                                estoque[categoria][modificar] = float(input("Digite o novo valor: "))
                                x = input("Valor atualizado com sucesso! digite qualquer tecla para voltar: ")

                            elif opcao == "2":
                                print("\n" * 50)
                                print('---= Remover Produto =---\n')
                                print("Selecione a categoria do produto\n")
                                
                                for i in estoque.keys():
                                    print(i)

                                categoria = input(": ")
                                print("\n")

                                print("Digite o item que deseja remover: ")
                                for item, valor in estoque[categoria].items():
                                    print(item, valor, "R$")             

                                
                                remover = input(": ")

                                del estoque[categoria][remover]
                                x = input("Item removido com sucesso! digite qualquer tecla para voltar: ")

                            elif opcao == "3":
                                print("\n" * 50)
                                print('---= Remover Categoria =---\n')
                                print("Selecione a categoria para remover\n")

                                for i in estoque.keys():
                                    print(i)

                                categoria = input(": ")
                                print("\n")

                                del estoque[categoria]
                                x = input("Categoria removida com sucesso! digite qualquer tecla para voltar: ")
                            elif opcao == "0":
                                break

                    elif res == "3": # adicionar produtos
                        while True:
                            print("\n" * 50)
                            print('---= Adicionar Produtos =---\n')
                            print("[0] Voltar")
                            print("[1] Adicionar produto")
                            print("[2] Adicionar categoria")
                            opcao = input(": ")

                            if opcao == "0":
                                break

                            elif opcao == "1":
                                print("\n" * 50)
                                print('---= Adicionar Produto =---\n')
                                
                                for i in estoque.keys():
                                    print(i)

                                print("Digite a categoria que deseja adicionar um produto")
                                categoria = input(": ")
                                print("\n")

                                novo_produto = input("Digite o novo produto: ")
                                novo_valor = float(input("Digite o novo valor: "))

                                estoque[categoria][novo_produto] = novo_valor
                                x = input("Produto adicionado com sucesso! digite qualquer tecla para voltar: ")

                            elif opcao == "2":
                                print("\n" * 50)
                                print('---= Adicionar Categoria =---\n')

                                print("Digite o nome da nova categoria")
                                nova_categoria = input(": ")
                                estoque[nova_categoria] = {}
                                x = input("Categoria adicionada com sucesso! digite qualquer tecla para voltar: ")

        except NameError:
            print("Nome ou cpf invalidos, tente novamente.")
            x = input(": ")


######################################################


    elif resposta == "3": # cadastrar
        print("\n" * 50)
        print("[0] voltar")
        print("[1] registrar funcionario")
        print("[2] registrar cliente")
        res = input(": ")

        if res == "1":
            print("\n" * 50)
            print("---= sistema de cadastro =---\n")
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            cpf = input("Digite seu cpf: ")
            print("\nFuncionario cadastrado com sucesso! digite qualquer tecla para voltar.")
            x = input(": ")

        elif res == "2": # não ficou claro o que eu faço com o cadastro do cliente :/
            print("\n" * 50)
            print("---= sistema de cadastro =---\n")
            clientenome = input("Digite seu nome: ")
            clientecpf = input("Digite seu cpf: ")
            print("\nCliente cadastrado com sucesso! digite qualquer tecla para voltar.")
            x = input(": ")