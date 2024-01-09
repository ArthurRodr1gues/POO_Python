class Pessoa:
    def __init__(self, nome, idade, sexo, altura): # Método construtor
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

pessoa1 = Pessoa('Fernando', 32, 'M', 1.90)
print(f'Bem vindo {pessoa1.nome}, parabéns pelos seus {pessoa1.idade} anos. Confirma '
      f'que seu sexo é {pessoa1.sexo} e sua altura {pessoa1.altura}?')