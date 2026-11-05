
import random
import math

# Gene Expression Programming (GEP)
# Target function: f(x) = x^2 + x + 1

POPULATION_SIZE = 30
GENERATIONS = 30
CHROMOSOME_LENGTH = 7
MUTATION_RATE = 0.10
CROSSOVER_RATE = 0.70

FUNCTIONS = ['+', '-', '*']
TERMINALS = ['x', '1', '2', '3']

def random_gene():
    return random.choice(FUNCTIONS + TERMINALS)


def create_chromosome():
    # Prefix expression representation
    return [
        random.choice(FUNCTIONS),
        random.choice(FUNCTIONS + TERMINALS),
        random.choice(FUNCTIONS + TERMINALS),
        random.choice(TERMINALS),
        random.choice(TERMINALS),
        random.choice(TERMINALS),
        random.choice(TERMINALS)
    ]


def evaluate(chromosome, x):
    """Evaluate a prefix expression tree."""
    position = [0]

    def parse():
        if position[0] >= len(chromosome):
            return 0

        gene = chromosome[position[0]]
        position[0] += 1

        if gene == 'x':
            return x
        elif gene in ['1', '2', '3']:
            return float(gene)

        left = parse()
        right = parse()

        if gene == '+':
            return left + right
        elif gene == '-':
            return left - right
        elif gene == '*':
            return left * right

        return 0

    try:
        result = parse()
        if not math.isfinite(result):
            return 1e10
        return result
    except (ValueError, OverflowError):
        return 1e10


def fitness(chromosome):
    error = 0

    for x in range(-5, 6):
        actual = x*x + x + 1
        predicted = evaluate(chromosome, x)
        error += abs(actual - predicted)

    return 1 / (1 + error)


def selection(population):
    return max(population, key=fitness)


def crossover(parent1, parent2):
    child = parent1[:]

    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child = parent1[:point] + parent2[point:]

    return child


def mutation(chromosome):
    child = chromosome[:]

    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            child[i] = random_gene()

    return child


def main():
    random.seed(42)

    population = [
        create_chromosome()
        for _ in range(POPULATION_SIZE)
    ]

    print("GENE EXPRESSION PROGRAMMING")
    print("Target Function: f(x) = x^2 + x + 1")
    print("--------------------------------")

    for generation in range(GENERATIONS):

        population.sort(key=fitness, reverse=True)

        best = population[0]

        if generation % 5 == 0:
            print(
                "Generation:", generation,
                "Fitness:", round(fitness(best), 6),
                "Chromosome:", best
            )

        new_population = [best[:]]

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)
            child = mutation(child)

            new_population.append(child)

        population = new_population

    best = max(population, key=fitness)

    print("\nBest Chromosome:", best)
    print("Best Fitness:", round(fitness(best), 6))

    print("\nPredicted and Actual Values:")

    for x in range(1, 6):
        predicted = evaluate(best, x)
        actual = x*x + x + 1

        print(
            "x =", x,
            "| Predicted =", round(predicted, 2),
            "| Actual =", actual
        )


if __name__ == "__main__":
    main()
