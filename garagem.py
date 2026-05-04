from veiculo import Veiculo, Carro, Moto
# Crie pelo menos 3 veículos (seus dados, não os do exemplo!)
v1 = Carro('Chevrolet', 'Onix', 2021, 4)
v2 = Moto('Yamaha', 'Fazer 250', 2020, 250)
v3 = Carro('Ford', 'Ka', 2019, 2)
v4 = Moto('Kawasaki', 'Ninja 300', 2023, 296)
v5 = Carro('Volkswagen', 'Gol', 2018, 4)
garagem = [v1, v2, v3, v4, v5]
# Percorra a lista e imprima cada veículo
for v in garagem:
 print(v)
# Imprima quantos são Carros e quantos são Motos
carros = [v for v in garagem if isinstance(v, Carro)]
motos = [v for v in garagem if isinstance(v, Moto)]
print(f'Carros: {len(carros)} | Motos: {len(motos)}')