
def bank(s, i=0.02, t=1):
    '''
    input: s(деньги),i(процент),t(срок хранения в банке)
    return: итоговый счет в банке
    '''
    if i > 0.05:
        print('Максимальный процент в нашем банке 5% годовых')
        return False
    savings = calculate_savings(s, i, t)
    return savings
def calculate_savings(savings, interest, time):
    '''
    input: savings(деньги),interest(процент),time(срок хранения в банке)
    return: savings с накопившимися процентами
    '''
    for i in range(time):
        savings += savings * interest
    return savings
savings = int(input('Сколько вы хотите положить денег в банк:'))
interest = int(input('Под какой процент вы хотите положить денги в банк:')) / 100
time = int(input('Насколько хотите положить денег в банк:'))
total_savings = bank(savings, interest, time)
if total_savings:
    print(f'Ваш итоговый счет в банке {total_savings}')

