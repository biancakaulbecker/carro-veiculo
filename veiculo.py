class Veiculo:
 def __init__(self, marca, modelo, ano):
  self._marca = marca
  self._modelo = modelo
  self.__ano = ano
@property
def marca(self):
 return self._marca
@property
def modelo(self):
 return self._modelo
@property
def ano(self):
 return self.__ano
def descrever(self):
 return f'{self.marca} {self.modelo} ({self.ano})'
def __str__(self):
 return self.descrever()

class Carro(Veiculo):
# herda Veiculo
 def __init__(self, marca, modelo, ano, num_portas):
# super() chama o __init__ do Pai
  super().__init__(marca, modelo, ano)
  self._num_portas = num_portas
@property
def num_portas(self):
 return self._num_portas
def descrever(self):
# SOBRESCREVE o Pai
 base = super().descrever()
 return f'{base} | {self.num_portas} portas'

class Moto(Veiculo):
# herda Veiculo

 def __init__(self, marca, modelo, ano, cilindradas):
  super().__init__(marca, modelo, ano)
  self._cilindradas = cilindradas
@property
def cilindradas(self):
 return self._cilindradas
def descrever(self):
# SOBRESCREVE o Pai
 base = super().descrever()
 return f'{base} | {self.cilindradas}cc'

# PASSO 3 - TESTES
c = Carro('Toyota', 'Corolla', 2023, 4)
m = Moto('Honda', 'CG160', 2022, 160)
print(c) # Toyota Corolla (2023) | 4 portas
print(m) # Honda CG 160 (2022) | 160cc
print(c, marca) # Toyota — herdado do Pai!
print(isinstance(c, Veiculo)) # True — Carro É UM Veiculo
print(isinstance(m, Carro)) # False — Moto NÃO é um Carro