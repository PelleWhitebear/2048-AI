from src.game.game_class import Game

# TODO: Implement GUI

if __name__ == '__main__':
    print("Start with AI? (y/n)")
    i = input().upper()

    if i == 'Y':
        print("choose AI type ( 1 Expectimax /  2 Mont Carlo Tree search)")
        X = input().upper()
        if X != '1' and X != '2':
            print("Invalid input")
            exit()
        game_module = Game(ai = True, ai_choice = int(X))
        
        
        
    elif i == 'N':
        game_module = Game()

    move_possible = True
    max_title = 0 
    while move_possible:
        if game_module.ai:
            move_possible, max_title = game_module.ai_move()

        else:
            move = input("Your move (W/A/S/D): ").strip().upper()
            if game_module.play(move):
                break
    print("Game Over")
    print("Total Score: ", max_title)
