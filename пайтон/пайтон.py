game_list = []

while True:
    game = input('''Какую игру вы хотите добавить в список?
Если закончили напишите - выход''')
    if game == 'выход':
        break
    rating = int(input('Какой у этой игры будет рейтинг?'))
    
    if game != 'выход':
        c = (game, rating)
        game_list.append(c)
        print(f'Текущий список игр содержит {game_list}')
        
   
       
    
    
    


                        



