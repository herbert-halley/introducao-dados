import os

tarefas = []


def adicionar_tarefa(tarefa):
    novaTarefa = (tarefa, "pendente")
    tarefas.append(novaTarefa)


def exibeTarefas(tarefa):
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
        return
    for tarefa in tarefas:
        print(f'tarefa: {tarefa[0]}, Status: {tarefa[1]}')


def concluirTarefa(tarefa):
    global tarefas
    tarefas = [(t[0], "concluída") if t[0] == tarefa else t for t
               in tarefas]


def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa]


def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0].lower() == tarefa.lower
                 ()]
    if resultado:
        for titulo, status in resultado:
            print(f'Tarefa nao encontrada: {titulo}, Status: {status}')
        else:
            print(f'Tarefa nao encontrada: {tarefa}')


while True:
    os.system('clear')

    print("\nMenu de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefas")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Buscar Tarefa")
    print("6. Sair")
    opcao = int(input('Escolha uma opcao: '))

    match opcao:
        case 1:
            tarefa = input('Digite a tarefa a ser adicionada: ')
            adicionar_tarefa(tarefa)
        case 2:
            exibeTarefas(tarefa)
        case 3:
            tarefa = input('Digite a tarefa a ser concluida: ')
            concluirTarefa(tarefa)
        case 4:
            tarefa = input('Digite a tarefa a ser removida: ')
            removerTarefa(tarefa)
        case 5:
            tarefa = input('Digite a tarefa a ser buscada: ')
            buscarTarefa(tarefa)
        case 6:
            print('Saindo do programa...')
            break
        case _:
            print('Opcao invalida. Tente novamente.')
    print()
    input('Pressione Enter para continuar...')
