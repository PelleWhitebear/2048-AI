from src.ai.weights import AIWeights
from src.game.game_class import Game

# TODO: Implement GUI

if __name__ == '__main__':
    print("Start with AI? (y/n)")
    i = input().upper()

    if i == 'Y':
        game_module = Game(ai = True, ai_search_depth=4)
        
        
        
    elif i == 'N':
        game_module = Game()

    move_possible = True
    max_title = 0 


  #  weights = AIWeights(w_open=3.5027765029028823, w_edge=-1.5104507118001784, w_mono=7.953022087585503, w_merge=7.958682579004645, w_empty=1.3038574960941691, SnakeMatrix=False) # matrix
    weights = AIWeights(w_open=12.331479240047372, w_edge=4.605457624021539, w_mono=-5.914482583951802, w_merge=6.201156747582119, w_empty=0.982279805907757, SnakeMatrix=True) # snake, best solution
    while move_possible:
        if game_module.ai:
            move_possible, max_title, total_sum = game_module.ai_move(weights)

        else:
            move = input("Your move (W/A/S/D): ").strip().upper()
            if game_module.play(move):
                break
    print("Game Over")
    print("Total Score: ", max_title)


def evaluate_performance_on_best_tiles(weights, num_games=1):
    dict = {}
    for i in range(num_games):
        game_module = Game(ai=True, ai_choice=1)
        move_possible = True
        max_title = 0
        total_sum = 0
        while move_possible:
            move_possible, max_title, total_sum = game_module.ai_move(weights)
        if max_title in dict:
            dict[max_title] += 1
        else: dict[max_title] = 1
    print(dict)
    return dict
        


    

