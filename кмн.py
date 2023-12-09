import random
import sys

print("КАМЕНЬ, НОЖНИЦЫ, БУМАГА")

# Количество побед, поражений и ничьих
wins = 0
losses = 0
ties = 0

while True:  # цикл игры
    print("%s побед, %s поражений, %s ничьих" % (wins, losses, ties))

    # цикл выбора игрока
    while True:
        print("Выберете ход: (к)амень, (н)ожницы, (б)умага / (в)ыход")
        playerMove = input()

        if playerMove == 'в':
            sys.exit()  # выход из программы

        if playerMove in {'к', 'н', 'б'}:
            break  # выход из цикла выбора хода
        print("Введите 'к', 'н' или 'б'.")

    # Выбор игрока
    if playerMove == 'к':
        print("КАМЕНЬ и ....")
    elif playerMove == 'н':
        print("НОЖНИЦЫ и ....")
    elif playerMove == 'б':
        print("БУМАГА и ....")

    # Выбор ПК
    computerMove = random.choice(['к', 'н', 'б'])
    if computerMove == 'к':
        print("КАМЕНЬ")
    elif computerMove == 'н':
        print("НОЖНИЦЫ")
    elif computerMove == 'б':
        print("БУМАГА")

    # Отображение и учет результата
    if playerMove == computerMove:
        print("Ничья!")
        ties += 1
    elif (playerMove == 'к' and computerMove == 'б') or \
         (playerMove == 'н' and computerMove == 'к') or \
         (playerMove == 'б' and computerMove == 'н'):
        print("Вы проиграли!")
        losses += 1
    else:
        print("Вы выиграли!")
        wins += 1

