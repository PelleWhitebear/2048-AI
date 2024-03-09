import cma
import numpy as np

# The objective function to maximize the highest tile number
def evaluate(board, w_open, w_edge, w_mono, w_merge, w_tile_flat, w_empty):
    # Here, you would implement your game simulation using the provided weights
    # and return the highest tile number achieved
    pass

# The wrapper for the objective function that will be used by CMA-ES
def objective_function(weights):
    # Assume board is the starting state of the board for evaluation
    board = start_game()  # This should reset/start the game and return the initial board

    # Extract individual weights from the flat weight list provided by CMA-ES
    w_open, w_edge, w_mono, w_merge, *w_tile_flat, w_empty = weights
    
    # Call the evaluation function with the current set of weights
    max_tile = evaluate(board, w_open, w_edge, w_mono, w_merge, w_tile_flat, w_empty)
    
    # Since CMA-ES is a minimization algorithm, negate the max_tile to make it a minimization problem
    return -max_tile

# Initialize the parameters for CMA-ES
initial_weights = [12, 5, -3.5, 4] + [1] * 16 + [1]  # Flat list including weights for the 4x4 w_tile matrix
sigma = 0.5  # Initial standard deviation
options = {'maxiter': 100, 'popsize': 10}  # Adjust as necessary

# Set up and run the optimizer
es = cma.CMAEvolutionStrategy(initial_weights, sigma, options)
while not es.stop():
    solutions = es.ask()
    es.tell(solutions, [objective_function(x) for x in solutions])
    es.logger.add()
    es.disp()

# Retrieve the results
result = es.result
best_weights = result[0]  # The best solution found (i.e., weights)
best_score = -result[1]  # The best score found (negate because we minimized the negative score)

print(f'Best weights: {best_weights}')
print(f'Best score (highest tile): {best_score}')
