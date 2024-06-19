
class Gatu:
    def __init__(self, nomegato, cor, peso): #recebe os parâmetros cor e sabor
        self.nomegato = nomegato
        self.cor = cor #esse tomate não tem métodos
        self.peso = peso

    def __repr__(self):#sempre criar o repr de uma classe
        return f"gato({self.nomegato}, {self.cor}, {self.peso})"


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


gato0 = Gatu('lua', 'branco', '20')
gato2 = Gatu('felpudo', 'amarelo', '35')
list_gato = [gato0, gato2]
#salva_lista(list_gato)
carrega_lista()
print(list_gato)