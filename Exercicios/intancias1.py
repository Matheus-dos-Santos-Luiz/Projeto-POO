class Restaurante:
    nome = ''
    categoria = '' 
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

categoria = Restaurante.categoria

restaurante_praca.nome = 'Bistrô'



print(f"Nome: {restaurante_pizza.nome} a categoria {restaurante_pizza.categoria}")
print(f"Nome do Restaurante: {restaurante_praca.nome}")
if restaurante_praca.ativo :
    print("Restaurante Ativo")
else:
    print("Inativo")

if restaurante_pizza.ativo :
    print("Restaurante Pizza Ativo")
else:
    print("Inativo")

