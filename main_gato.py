from gatoto import Gatu
def adicionar_usuario(usuarios):
    nome = input("Nome do pet: ")
    senha = input("Senha: ")
    self.append(Gatu(nome, senha))

def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in self:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def main():
    print("Bem-vindo a Clínica de Gatos!\n")
    print("Escolha o que deseja fazer: \n1.Login \n2.Adicionar Gato \n3.Sair")
    escolha = int(input("Escolha a alternativa desejada: "))
    match escolha:
        case 1:
            adicionar_usuario(usuarios)
        case 2:
            login(usuarios)

        case 3:
            print("Fechando...")
            quit
        case _:
            print("\nALGO ESTÁ INCORRETO, TENTE NOVAMENTE!\n")
            quit

if __name__ == "__main__":
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