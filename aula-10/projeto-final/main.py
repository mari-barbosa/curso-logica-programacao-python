# --- CRIANDO A LISTA ---
tarefas = []


# --- FUNÇÕES DO NOSSO PROGRAMA ---
def adicionar_tarefa():
    nova_tarefa = input("Digite a descrição da nova tarefa: ").strip()
    if nova_tarefa != "":
        tarefas.append(nova_tarefa)
        print(f"✓ Tarefa '{nova_tarefa}' adicionada com sucesso!")
    else:
        print("⚠ A tarefa não pode estar vazia.")


def listar_tarefas():
    if len(tarefas) == 0:
        print("\nNenhuma tarefa cadastrada no momento.")
    else:
        print("\n--- SUAS TAREFAS ---")
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f"{indice}. {tarefa}")


def remover_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        try:
            num = int(input("\nDigite o número da tarefa que deseja remover: "))
            if 1 <= num <= len(tarefas):
                removida = tarefas.pop(num - 1)
                print(f"✓ Tarefa '{removida}' removida com sucesso!")
            else:
                print("⚠ Número de tarefa inválido.")
        except ValueError:
            print("⚠ Por favor, digite um número válido.")


# --- MENU PRINCIPAL ---
def exibir_menu():
    print("\n==============================")
    print("    GERENCIADOR DE TAREFAS    ")
    print("==============================")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")


# --- PROGRAMA PRINCIPAL ---
opcao = ""
while opcao != "4":
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("\nEncerrando o Gerenciador... Parabéns por concluir o curso! 🚀")
    else:
        print("⚠ Opção inválida! Tente novamente.")