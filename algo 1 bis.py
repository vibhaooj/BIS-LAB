# Genetic Algorithm

# Step 1: Initial population
population = ["1010", "1100", "0110", "1001"]


# Fitness function
def fitness(chromosome):
    return int(chromosome, 2)


# Step 2: Calculate fitness
fitness_values = {}

for chromosome in population:
    fitness_values[chromosome] = fitness(chromosome)


print("Genetic Algorithm")
print("\nInitial population:")
for chromosome in population:
    print(chromosome, "=", fitness(chromosome))


# Step 3: Select best chromosomes
population.sort(
    key=lambda chromosome: fitness(chromosome),
    reverse=True
)

parent1 = population[0]
parent2 = population[1]

print("\nFitness Values:")
for chromosome in ["1010", "1100", "0110", "1001"]:
    print(chromosome, "=", fitness(chromosome))

print("\nGeneration 1:")
print("Selection:", parent1, ",", parent2)


# Step 4: Crossover
# Crossover point = 2
crossover_point = 2

child1 = (
    parent1[:crossover_point]
    + parent2[crossover_point:]
)

child2 = (
    parent2[:crossover_point]
    + parent1[crossover_point:]
)

print("Crossover:", child1, ",", child2)


# Step 5: Mutation
# Mutate the last bit of child1
child1 = child1[:-1] + "1"

print("Mutation:", child1, ",", child2)


# Step 6: Create next generation
new_population = [
    child1,
    child2
]


# Generation 2
print("\nGeneration 2:")

# Find best chromosome
best_chromosome = max(
    new_population,
    key=fitness
)

best_fitness = fitness(best_chromosome)

print("Best chromosome:", best_chromosome)
print("Fitness value:", best_fitness)

print("Optimal solution found:", best_chromosome)
print("Maximum fitness:", best_fitness)
