from gatoto_usuario import Usuario
from gatoto_info import Info
def ler_dados():
    usuarios = []
    infos = []
    try:
        with open('gato_ativ/dados.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('usuario:'):
                    user_data = line.split('usuario:')[1]
                    usuarios.append(Usuario.from_string(user_data))
                elif line.startswith('informacoes:'):
                    info_data = line.split('informacoes:')[1]
                    infos.append(Info.from_string(info_data))

    except FileNotFoundError:
        pass
    return usuarios, infos

def salvar_dados(usuarios, informacoes):
    with open('gato_ativ/dados.txt', 'a') as file:
        for user in usuarios:
            file.write(f'usuario:{user}\n')
        for task in informacoes:
            file.write(f'Informacoes:{task}\n')

def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def adicionar_usuario(usuarios):
    nome = input("Novo nome de usuário: ")
    senha = input("Nova senha: ")
    usuarios.append(Usuario(nome, senha))

def main():
    usuarios, infos = ler_dados()
    print("Bem-vindo a Clínica de Gatos!\n")
    print("Escolha o que deseja fazer: \n1.Adicionar Usuário \n2.Login \n3.Sair")
    escolha = int(input("Escolha a alternativa desejada: "))

    match escolha:
            case 1:
                adicionar_usuario(usuarios)
                salvar_dados(usuarios, infos)
            case 2:
                login(usuarios)
                while True:
                    print("Login realizado com sucesso!")
                    print("1. Ver Informações do Pet\n2. Adicionar Informações de seu gato\n3. Sair\n")
                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                            for info in infos:
                                print(info)
                            if not info in infos:
                                print("Não há informações de seu pet. Adicione por favor!")
                                return
                        
                    if opcao == '2':
                        print("Informações do pet:\n")
                        
                        info_gato = input("Adicione nome, peso e cor do seu pet: ")
                        infos.append(Info(info_gato))

                    elif opcao == '3':
                        salvar_dados(usuarios, infos)
                        print("Dados salvos. Saindo...")
                        break
                    else:
                        print("Opção inválida.")

                if not login(usuarios):
                    print("Usuário ou senha incorretos.")
                    return main()

            case 3:
                print("Fechando...")
                quit

            case _:
                print("\nALGO ESTÁ INCORRETO, TENTE NOVAMENTE!\n")
                quit

main()



'''
def salva_lista(lista:list):

        with open('gato_ativ/dados.txt', 'w') as file: #with cria um alias apelido para o arquivo tomate.txt dizendo que vamos nos referir ao arquivo como a variável file
            #w significa modo de escrita
            for gato in lista:
                file.write(f'Nome do pet: {gato.nomegato}, Cor: {gato.cor}, Peso: {gato.peso}\n') # \n pula a linha

def carrega_lista():
        with open('gato_ativ/dados.txt', 'r') as file:
            lines = file.readlines() #a variável linhas tem o valor de lista onde cada item é uma linha do arquivo
        for line in lines: #Line apresenta uma linha das lines
            data = line.strip().split(', ') #usamos o strip para remover caracteres especiais como /n e o split para dividir os valores depois da string "', '"
            nomegato = data[0].split(': ')[1]
            cor = data[1].split(': ')[1]
            peso = data[2].split(': ')[1]
            gato1 = Gatu(nomegato, cor, peso)#
            list_gato.append(gato1) #adicionar um tomate na lista de tomate e assim é carregado os tomates para a variável list_tomate

        for gato1 in list_gato:
            print(f'Nome do pet: {gato1.nomegato}, Cor: {gato1.cor}, Peso: {gato1.peso}')


gatoadm = Gatu('lua', 'branco', '20')
list_gato = [gatoadm]
salva_lista(list_gato)
print(list_gato)
carrega_lista()
print(list_gato)

'''