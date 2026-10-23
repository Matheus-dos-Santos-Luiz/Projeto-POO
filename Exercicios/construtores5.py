#1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
#2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.   
    def __str__(self):
        return f' O {self._titulo} do {self._autor}, publicado em {self._ano_publicacao}'

#livro1 = Livro('The Egoist', 'Neo', '2022')
#livro2 = Livro('Liga Neo Egoist', 'Neo', '2024')
# 
# print(livro1)
# print(livro2)

#3.Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def emprestar(self):
        self._disponivel = False

#livro3 = Livro('Japão X França' , 'Neo' , '2026')
#print(f'Antes {livro3._disponivel}')
#livro3.emprestar()
#print(f'Agora {livro3._disponivel}')


#4.Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

# Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros

# 5) Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.