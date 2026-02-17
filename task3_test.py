world_champions = {
    2002: 'Бразилия',
    2006: 'Греция',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Греция'
for key, value in world_champions.items():
    print(f'{key} - {value}')

country = 'Италия'

def check_wch():
    for value in world_champions.values():
        if value == country:
            print('Италия становилась чемпионом в 21 веке!')
            break 
    else:
        print('Италия не становилась чемпионом в 21 веке!')

check_wch()