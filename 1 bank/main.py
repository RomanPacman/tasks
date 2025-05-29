def bank (a , years):
    print(f'Сумма вкалада: {a}, срок вклада: {years} год(-а)/лет')
    for year in range(years):
        a = round(a + a * 0.1, 1)
        print(f'После {year+1} лет сумма на счету: {a}')

bank(10,4)
