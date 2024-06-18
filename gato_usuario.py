class Gatoo:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def __repr__(self):
        return f"{self.nome}, {self.peso}"
    
    @staticmethod
    def from_string(user_str):
        nome, peso = user_str.split(',')
        return Gatoo(nome, peso)