
rendimento = int(input('Qual o rendimento da lata ='))
altura = int(input('Altura da parede ='))
largura = int(input('largura da parede ='))


def calculo_tinta():
    area = altura * largura
    total = area /rendimento
    print(f'Você precisará de {total} latas de tinta')

calculo_tinta()