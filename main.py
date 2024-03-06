from src.game.game_class import Game

# TODO: Implement GUI

if __name__ == '__main__':
    print("Start with AI? (y/n)")
    i = input().upper()

    if i == 'Y':
        print("AI not implemented yet...")
        game_module = Game(ai = True)
        
        
        
    elif i == 'N':
        game_module = Game()

    while True:
        if game_module.ai:
            game_module.ai_move()
        else:
            move = input("Your move (W/A/S/D): ").strip().upper()
            if game_module.play(move):
                break
