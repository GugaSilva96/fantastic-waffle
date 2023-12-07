def exibir_mensagem_inicial():
    print("Olá, eu sou a assistente virtual de pedidos do restaurante Comida Boa. Gostaria de fazer seu pedido?")

# Responde à primeira mensagem
exibir_mensagem_inicial()

# Espera a resposta do usuário
resposta = input("Sua resposta (sim/não): ")

# Verifica a resposta
if resposta.lower() == "sim":
    print("Primeiramente, nos passe seu nome e telefone de contato.")
    nome = input("Seu nome: ")
    telefone = input("Seu telefone: ")

    print("Agora escolha sua proteína (frango ou carne): ")
    proteina = input("Sua escolha: ")

    if proteina.lower() not in ["frango", "carne"]:
        print("Favor escolher entre frango ou carne.")
        exibir_mensagem_inicial()
    else:
        print("Agora escolha seu acompanhamento (farofa, batata ou arroz): ")
        acompanhamento = input("Sua escolha: ")

        if acompanhamento.lower() not in ["farofa", "batata", "arroz"]:
            print("Favor escolher entre farofa, batata ou arroz.")
            exibir_mensagem_inicial()
        else:
            print("Ótimo! Agora, por favor, forneça o endereço para entrega.")
            endereco = input("Seu endereço: ")

            # Mensagem de confirmação
            confirmacao = f"Confirme os dados:\nNome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nPedido: {proteina} com {acompanhamento}\nOs dados estão corretos? (sim/não)"
            print(confirmacao)

            # Espera a resposta do usuário
            resposta_confirmacao = input("Sua resposta: ")

            # Verifica a confirmação
            if resposta_confirmacao.lower() == "sim":
                print("Ótimo! O seu pedido está em fase de preparo e logo sairá para entrega.")
                # Envia mensagem de confirmação para a impressora na rede
                mensagem_impressora = f"Novo pedido:\nNome: {nome}\nTelefone: {telefone}\nEndereço: {endereco}\nPedido: {proteina} com {acompanhamento}"
                # Adicione aqui o código para enviar a mensagem para a impressora na rede
            else:
                print("Por favor, refaça seu pedido.")
                exibir_mensagem_inicial()
else:
    print("Conversa encerrada. Se precisar de ajuda, estamos à disposição.")
    exibir_mensagem_inicial()
