# Sistema de reservas de cinema sem funções

# Dados iniciais
disponibilidade_salas = {
    "Sala 1": ["Livre" for _ in range(10)],  # 10 assentos por sala
    "Sala 2": ["Livre" for _ in range(10)],
    "Sala 3": ["Livre" for _ in range(10)],
}

reservas = []  # Lista para armazenar as reservas

while True:
    print("\n==== Sistema de Reservas de Cinema ====")
    print("1. Exibir disponibilidade das salas")
    print("2. Reservar um assento")
    print("3. Exibir reservas realizadas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nDisponibilidade das Salas:")
        for sala, assentos in disponibilidade_salas.items():
            print(f"{sala}: {', '.join(assentos)})")

    elif opcao == "2":
        sala = input("Digite o nome da sala (Sala 1, Sala 2, Sala 3): ")
        if sala not in disponibilidade_salas:
            print("Sala inválida.")
            continue

        print(f"\nAssentos livres em {sala}:")
        for i, status in enumerate(disponibilidade_salas[sala]):
            print(f"Assento {i + 1}: {status}")

        try:
            assento = int(input("Escolha o número do assento (1-10): ")) - 1
            if assento < 0 or assento >= len(disponibilidade_salas[sala]):
                print("Número de assento inválido.")
                continue
            if disponibilidade_salas[sala][assento] == "Reservado":
                print("Assento já está reservado.")
                continue

            nome_cliente = input("Digite o nome do cliente: ")
            disponibilidade_salas[sala][assento] = "Reservado"
            reservas.append({"sala": sala, "assento": assento + 1, "cliente": nome_cliente})
            print(f"Reserva concluída para {nome_cliente} no {sala}, assento {assento + 1}.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    elif opcao == "3":
        print("\nReservas realizadas:")
        if not reservas:
            print("Nenhuma reserva feita ainda.")
        else:
            for reserva in reservas:
                print(f"Cliente: {reserva['cliente']}, Sala: {reserva['sala']}, Assento: {reserva['assento']}")

    elif opcao == "4":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
