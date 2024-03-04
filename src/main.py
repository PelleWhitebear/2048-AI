from game.game_class import Game

# TODO: Implement GUI

if __name__ == '__main__':
    print("Start with AI? (y/n)")
    i = input().upper()

    if i == 'Y':
        print("AI not implemented yet...")
    elif i == 'N':
        game_module = Game()

    while True:
        i = input()
        if game_module.play(i):
            break
