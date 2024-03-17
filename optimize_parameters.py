import cma
from matplotlib import pyplot as plt
from tqdm import tqdm
from src.game.game_class import Game
from src.ai.weights import AIWeights  # Make sure this path matches your project structure

def evaluate(game_instance: Game, weights: AIWeights):
    # Initialize the highest tile as the minimum possible value
    highest_tile = 2
    highest_sum = 2
    move_possible = True
    
    while move_possible:
        # Assuming game_instance.ai_move now accepts an instance of AIWeights
        move_possible, highest_tile, highest_sum = game_instance.ai_move(weights)
    
    return highest_sum

def objective_function(weights_array):
    # Create an AIWeights instance from the array provided by CMA-ES
    ai_weights = AIWeights(*weights_array)
    
    # Initialize the game instance
    game_instance = Game(ai=True, ai_choice=1, print_board_bool=False, search_depth=2)

    # Evaluate the game performance using the provided weights
    max_tile = evaluate(game_instance, ai_weights)
    
    # Negate the max_tile value to turn maximization into minimization for CMA-ES
    return -max_tile

# Initial parameters for CMA-ES
initial_weights = [0, 0, 0, 0, 0]  # Initial values for w_open, w_edge, w_mono, and w_merge, w_empty / snake
sigma = 1  # Initial standard deviation for the distribution
options = {'maxiter': 800, 'popsize': 12}  # Adjust these options based on your needs

# Run the optimization with a progress indicator
es : cma.CMAEvolutionStrategy = cma.CMAEvolutionStrategy(initial_weights, sigma, options)
max_iter = options['maxiter']  # Maximum number of iterations

with tqdm(total=max_iter, desc="Optimizing", unit="iter") as pbar:
    while not es.stop():
        solutions = es.ask()
        es.tell(solutions, [objective_function(x) for x in solutions])
        pbar.update(1)  # Update the progress bar for each iteration

# Retrieve and print the results
result = es.result
best_weights_array = result[0]  # Best found solution (array of weights)
best_score = -result[1]  # Best score found; negate it to match the original maximization goal



# Convert the best weights array back to an AIWeights instance for readability
best_weights = AIWeights(*best_weights_array)

print(f'Best weights array: {best_weights_array}')
print(f'Best AIWeights instance: {best_weights}')
print(f'Best score (highest tile achieved): {best_score}')

es.plot()

# Save the plot as an image file
plt.savefig('optimization_progress.png')
plt.close()