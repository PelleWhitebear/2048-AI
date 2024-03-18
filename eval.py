from src.ai.weights import AIWeights
from src.game.game_class import Game


def evaluate_performance_on_best_tiles(weights, num_games=20, depth=1):
    dict = {}
    
    for i in range(num_games):
        game_module = Game(ai=True, print_board_bool=False, ai_search_depth=depth)
        move_possible = True
        max_title = 0
        total_sum = 0
        while move_possible:
            move_possible, max_title, total_sum = game_module.ai_move(weights)
        if max_title in dict:
            dict[max_title] += 1
        else: dict[max_title] = 1
    print("\n -- search depth" )
    print(depth)
    print(dict)
    print("\n --")
    return dict

#weights = AIWeights(w_open=-0.8039602964183975, w_edge=1.9012526196346125, w_mono=-2.121449014193914, w_merge=2.8562552983851712, w_empty=0.6750731046374948)
weights = AIWeights(w_open=12.331479240047372, w_edge=4.605457624021539, w_mono=-5.914482583951802, w_merge=6.201156747582119, w_empty=0.982279805907757) # snake
#weights = AIWeights(w_open=0.7932106804266141, w_edge=-1.8122963456784016, w_mono=-2.826612224485512, w_merge=2.5880246946301564, w_empty=2.816131262925884) 
#weights = AIWeights(w_open=3.5027765029028823, w_edge=-1.5104507118001784, w_mono=-7.953022087585503, w_merge=7.958682579004645, w_empty=1.3038574960941691) # matrix eval
#for i in range(4,5):
evaluate_performance_on_best_tiles(weights, 100, 4)