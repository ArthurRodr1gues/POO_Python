class Pessoa:
    nome = 'Padrão'

pessoa1=Pessoa() #criação do objeto / Instanciamento
print (pessoa1.nome) # monstrando que o atributo nome está sendo puxado por padrão pois está no corpo da classe
pessoa1.nome = 'Fernando' # Modificando o atributo nome sem alterar o corpo da classe
print (pessoa1.nome) # Mostrando que a alteração anterior realmente funcionou. (Será impresso 'Fernando' na tela)