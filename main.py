import ler_dados
from gato_usuario import Gatoo

def adicionar_usuario(adicionar):
    print("Bem-vindo a Clínica de Gatos")
    nome_g = input("Qual é o nome do gato(a)? ")
    peso_g = input("Qual é o peso do gato(a)? ")

    adicionar.append(Gatoo(nome_g, peso_g))



def salvar_dados(usuarios, tarefas):
    with open('projeto/dados.txt', 'w') as file:
        for user in usuarios:
            file.write(f'usuario: {user}\n')
        for task in tarefas:
            file.write(f'tarefa: {task}\n')

def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def adicionar_usuario(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    usuarios.append(Usuario(nome, senha))

def main():
    usuarios, tarefas = ler_dados()
    
    if not login(usuarios):
        print("Usuário ou senha incorretos.")
        return
    
    print("Login realizado com sucesso!")
    while True:
        print("\n1. Adicionar Tarefa\n2. Ver Tarefas\n3. Adicionar Usuário\n4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            descricao = input("Descrição da tarefa: ")
            tarefas.append(Tarefa(descricao))
        elif opcao == '2':
            for tarefa in tarefas:
                print(tarefa)
        elif opcao == '3':
            adicionar_usuario(usuarios)
        elif opcao == '4':
            salvar_dados(usuarios, tarefas)
            print("Dados salvos. Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
