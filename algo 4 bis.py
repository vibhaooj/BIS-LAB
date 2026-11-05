import random
import math


# Objective function
def objective_function(solution):
    x = solution[0]
    y = solution[1]

    return x * x + y * y


# Generate new solution using random search step
def generate_new_solution(solution, best_solution):
    new_solution = []

    for i in range(2):
        step = random.uniform(-1, 1)

        value = solution[i] + step * (solution[i] - best_solution[i])

        # Keep within limits
        value = max(-5, min(5, value))

        new_solution.append(value)

    return new_solution


# Cuckoo Search
def cuckoo_search():

    # Parameters
    n_nests = 25
    max_iterations = 500
    discovery_probability = 0.25

    lower_bound = -5
    upper_bound = 5

    # Step 1: Initialize nests randomly
    nests = []

    for i in range(n_nests):
        solution = [
            random.uniform(lower_bound, upper_bound),
            random.uniform(lower_bound, upper_bound)
        ]

        nests.append(solution)

    # Find initial best solution
    best_solution = min(nests, key=objective_function)
    best_fitness = objective_function(best_solution)

    # Main loop
    for iteration in range(1, max_iterations + 1):

        # Step 3: Generate new solutions
        new_nests = []

        for i in range(n_nests):

            new_solution = generate_new_solution(
                nests[i],
                best_solution
            )

            new_nests.append(new_solution)

        # Step 4: Replace existing solution if better
        for i in range(n_nests):

            random_nest = random.randint(0, n_nests - 1)

            if objective_function(new_nests[i]) < objective_function(nests[random_nest]):

                nests[random_nest] = new_nests[i]

        # Step 5: Abandon some nests
        for i in range(n_nests):

            if random.random() < discovery_probability:

                # Step 6: Generate a new nest
                nests[i] = [
                    random.uniform(lower_bound, upper_bound),
                    random.uniform(lower_bound, upper_bound)
                ]

        # Update best solution
        current_best = min(nests, key=objective_function)
        current_fitness = objective_function(current_best)

        if current_fitness < best_fitness:

            best_solution = current_best.copy()
            best_fitness = current_fitness

        # Print every 100 iterations
        if iteration % 100 == 0:

            print(
                "Iteration",
                iteration,
                ": Best fitness =",
                round(best_fitness, 8)
            )

    return best_solution, best_fitness


# Main program
best_solution, best_fitness = cuckoo_search()


print("\n----- Cuckoo Search Results -----")

print(
    "Best solution :",
    [round(x, 8) for x in best_solution]
)

print(
    "Minimum objective value =",
    round(best_fitness, 10)
)
