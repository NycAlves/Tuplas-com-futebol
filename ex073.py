n = 'Palmeiras', 'Corinthians', 'Atlético PR', 'Atlético MG', 'Internacional', 'Fluminense', 'Botafogo', 'Santos', 'Bragantino', 'São Paulo', 'Avaí', 'Atlético GO', 'Ceará', 'Flamengo', 'Coritiba','América MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude'
print(f'Lista de times do brasileirão: {n}')
print('-='*30)
print(f'Os 5 primeiros são: {n[0:5]}')
print('-='*30)
print(f'Os 4 últimos são: {n[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(n)}')
print(f'O Avaí está na {n.index("Avaí")+1} posição')
