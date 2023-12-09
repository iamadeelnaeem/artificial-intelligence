import random


NUM_QUEENS = 8

POPULATION_SIZE = 8

MUTATION_RATE = 5

def generate_random_board():
    # Generate a random board state with queens placed in each column
    board = [random.randint(0, NUM_QUEENS - 1) for _ in range(NUM_QUEENS)]
    return board

def initial_random_population_generator():
    # Generate an initial population of random board states
    population = [generate_random_board() for _ in range(POPULATION_SIZE)]
    return population

def fitness(board):
    # Calculate the fitness of a board state (number of non-attacking pairs of queens)
    attacks = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                attacks += 1
    #total no of non attacking queens can be 28
    #if we minus atacks from it remaing will be non attacking left
    return 28 - attacks

def random_parent_selector(population):
    # Select a random parent from the population based on fitness proportionate selection
    fitness_values = [fitness(board) for board in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness_value / total_fitness for fitness_value in fitness_values]
    return random.choices(population, probabilities)[0]

def crossover(parent1, parent2):
    # Perform crossover to generate a child from two parents
    crossover_point = random.randint(1, NUM_QUEENS - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(board):
    # Perform mutation on a board state
    if random.randint(1, 100) > MUTATION_RATE:
        return board
    mutated_board = list(board)
    queen_col = random.randint(0, NUM_QUEENS - 1)
    mutated_board[queen_col] = random.randint(0, NUM_QUEENS - 1)
    return mutated_board

def genetic_algorithm():
    population = initial_random_population_generator()
    generations = 0
    while True:
        print(f"Generation: {generations}")
        for board in population:
            print(board)
        print("\n")
        generations += 1
        fitness_values = [fitness(board) for board in population]
        if max(fitness_values) == 28:
            # for i in range(len(fitness_values)):
            #     if max(fitness_values) == 28:
            #         print(fitness_values[i])
            print("Solution found!")
            break
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1 = random_parent_selector(population)
            parent2 = random_parent_selector(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population

genetic_algorithm()
