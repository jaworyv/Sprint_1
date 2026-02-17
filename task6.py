types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

used = set()
new_value = []

for key, value in tickets.items():
    for v in value:
        if v not in used:
            new_value.append(v)
        used.add(v)
    tickets[key] = new_value
    new_value = []

print(tickets)