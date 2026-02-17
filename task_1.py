dano = '1h 45m,360s,25m,30m 120s,2h 60s'
dano2 = dano.replace(' ', ',')
dano3 = dano2.split(',')
answer = []
for d in dano3:
    if 's' in d:
        s1 = d.replace('s', '')
        s2 = int(s1) / 60
        answer.append(s2)
    elif 'h' in d:
        h1 = d.replace('h', '')
        h2 = int(h1) * 60
        answer.append(h2)
    elif 'm' in d:
        m1 = d.replace('m', '')
        answer.append(int(m1))

result = sum(answer)

print(result)
    