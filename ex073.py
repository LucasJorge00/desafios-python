# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Os 5 primeiros.
# B) Os últimos 4 colocados.
# C) Times em ordem alfabética.
# D) Em que posição está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia',
'São Paulo', 'Fluminense', 'Sport Recife'
'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A chapecoense está na {times.index("Chapecoense") + 1}° posição')
