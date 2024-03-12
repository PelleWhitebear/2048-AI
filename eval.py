from src.ai.weights import AIWeights
from src.game.game_class import Game


def evaluate_performance_on_best_tiles(weights, num_games=20):
    dict = {}
    for i in range(num_games):
        game_module = Game(ai=True, ai_choice=1, print_board_bool=False)
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

weights = AIWeights(w_open=5.336521160788287, w_edge=1.227927904779254, w_mono=-2.2908727512303084, w_merge=3.115830573443014)
evaluate_performance_on_best_tiles(weights, 20)