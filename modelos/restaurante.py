from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title() 
        self._categoria = categoria.upper() 
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
            return f'{self._nome} | {self._categoria}'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            # Corrigir aqui: de media_avalicoes para media_avaliacoes
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'  

    def alternar_estado(self):
          self._ativo  = not self._ativo
     
    def receber_avaliacao(self, cliente, nota):
        if   nota < 0 or nota > 5:
            return f'Essa nota não é permitida, poderia reavaliar com uma nota de 0 a 5 ?'
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
            if not self._avaliacoes:
                return 'Ainda não há avaliações'
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            quantidade_de_notas = len(self._avaliacoes)
            media = round(soma_das_notas / quantidade_de_notas, 1)
            return media
#restaurante_praca = Restaurante('Praça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
#
#Restaurante.listar_restaurantes()


## Desafio final 
#  Olá! Compreendo que você esteja com dificuldades para assistir ao vídeo e gostaria de um resumo #  para acompanhar as sugestões e soluções apresentadas na aula.
#  
#  Nesta aula, o instrutor demonstrou como aplicar melhorias no projeto, focando em duas questões #  principais:
#  
#  Exibir um traço quando não há avaliações:
#  
#  Anteriormente, se um restaurante não tivesse avaliações, a média retornava 0.
#  A solução foi modificar o método media_avaliacoes no arquivo restaurante.py. Se a lista de #  avaliações estiver vazia, ele agora retorna a string '-' (um traço) em vez de 0.
#  Isso foi testado comentando as linhas de código que adicionavam avaliações no app.py e #  executando o programa.
#  Validar as notas das avaliações:
#  
#  O objetivo era garantir que as notas recebidas estivessem dentro de um intervalo específico #  (neste caso, entre 0 e 5).
#  A solução foi adicionar uma condição if no método receber_avaliacao no arquivo restaurante.py.
#  Agora, uma avaliação só é adicionada à lista _avaliacao se a nota estiver entre 0 e 5 #  (exclusivo de 0 e inclusivo de 5).
#  Isso foi demonstrado com notas como 10, 8 e 2, onde apenas a nota 2 foi aceita e refletida na #  média final, pois as outras estavam fora do intervalo definido.
#  Essas foram as duas melhorias abordadas na aula, mostrando como resolver os problemas #  levantados no vídeo anterior. Lembre-se que existem diversas maneiras de resolver esses #  problemas, e esta foi uma das abordagens apresentadas.
#  
#  Espero que este resumo ajude você a entender o conteúdo da aula! Se tiver mais alguma dúvida #  específica sobre esses pontos, é só perguntar.