import cma
from src.game.game_class import Game
from src.ai.weights import AIWeights  # Make sure this path matches your project structure

def evaluate(game_instance: Game, weights: AIWeights):
    # Initialize the highest tile as the minimum possible value
    highest_tile = 2
    move_possible = True
    
    while move_possible:
        # Assuming game_instance.ai_move now accepts an instance of AIWeights
        move_possible, highest_tile = game_instance.ai_move(weights)
    
    return highest_tile

def objective_function(weights_array):
    # Create an AIWeights instance from the array provided by CMA-ES
    ai_weights = AIWeights(*weights_array)
    
    # Initialize the game instance
    game_instance = Game(ai=True, ai_choice=1)

    # Evaluate the game performance using the provided weights
    max_tile = evaluate(game_instance, ai_weights)
    
    # Negate the max_tile value to turn maximization into minimization for CMA-ES
    return -max_tile

# Initial parameters for CMA-ES
initial_weights = [1, 1, 1, 1]  # Initial values for w_open, w_edge, w_mono, and w_merge
sigma = 0.5  # Initial standard deviation for the distribution
options = {'maxiter': 100, 'popsize': 8}  # Adjust these options based on your needs

# Run the optimization
es = cma.CMAEvolutionStrategy(initial_weights, sigma, options)
while not es.stop():
    solutions = es.ask()
    es.tell(solutions, [objective_function(x) for x in solutions])
    es.logger.add()
    es.disp()

# Retrieve and print the results
result = es.result
best_weights_array = result[0]  # Best found solution (array of weights)
best_score = -result[1]  # Best score found; negate it to match the original maximization goal

# Convert the best weights array back to an AIWeights instance for readability
best_weights = AIWeights(*best_weights_array)

print(f'Best weights: {best_weights_array}')
print(f'Best weights: {best_weights}')
print(f'Best score (highest tile achieved): {best_score}')
