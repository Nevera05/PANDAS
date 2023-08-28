import pandas as pd

automoveis = pd.read_csv('marcas-carro-tratada.csv', sep=';')

marca = 'CHEVROLET'

carro = automoveis.loc[automoveis['nome'] == marca, ['id', 'nome'] ]

print(carro)

marca = 'HONDA'

carro = automoveis.loc[automoveis['nome'] == marca, ['id', 'nome'] ]

print(carro)

marca = 'DAIHATSU'

carro = automoveis.loc[automoveis['nome'] == marca, ['id', 'nome'] ]

print(carro)