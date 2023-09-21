shop_list = []
while True:
    products = input('''Что вы хотите добавить в список?
Если закончили напишите - выход''')
    if products != 'выход':
        shop_list.append(products)
        print(f'список покупок {shop_list}')
    if products == 'выход':
        break
        
