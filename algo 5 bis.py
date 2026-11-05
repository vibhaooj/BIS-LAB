import random
import math


# Objective function
def objective_function(position):
    x = position[0]
    y = position[1]

    return x * x + y * y


# Grey Wolf Optimization
def gwo():

    # Parameters
    n_wolves = 20
    max_iterations = 500

    lower_bound = -10
    upper_bound = 10

    # Step 1: Initialize population of grey wolves randomly
    wolves = []

    for i in range(n_wolves):
        wolf = [
            random.uniform(lower_bound, upper_bound),
            random.uniform(lower_bound, upper_bound)
        ]

        wolves.append(wolf)

    # Initialize Alpha, Beta and Delta
    alpha = [0, 0]
    beta = [0, 0]
    delta = [0, 0]

    alpha_fitness = float("inf")
    beta_fitness = float("inf")
    delta_fitness = float("inf")

    # Main loop
    for iteration in range(max_iterations):

        # Step 2: Calculate fitness of each wolf
        for wolf in wolves:

            fitness = objective_function(wolf)

            # Step 3: Identify Alpha, Beta and Delta
            if fitness < alpha_fitness:

                delta_fitness = beta_fitness
                delta = beta.copy()

                beta_fitness = alpha_fitness
                beta = alpha.copy()

                alpha_fitness = fitness
                alpha = wolf.copy()

            elif fitness < beta_fitness:

                delta_fitness = beta_fitness
                delta = beta.copy()

                beta_fitness = fitness
                beta = wolf.copy()

            elif fitness < delta_fitness:

                delta_fitness = fitness
                delta = wolf.copy()

        # Step 5: Decrease parameter a gradually
        a = 2 - iteration * (2 / max_iterations)

        # Step 4: Update positions of all wolves
        for i in range(n_wolves):

            for j in range(2):

                # Alpha wolf
                r1 = random.random()
                r2 = random.random()

                A1 = 2 * a * r1 - a
                C1 = 2 * r2

                D_alpha = abs(C1 * alpha[j] - wolves[i][j])

                X1 = alpha[j] - A1 * D_alpha

                # Beta wolf
                r1 = random.random()
                r2 = random.random()

                A2 = 2 * a * r1 - a
                C2 = 2 * r2

                D_beta = abs(C2 * beta[j] - wolves[i][j])

                X2 = beta[j] - A2 * D_beta

                # Delta wolf
                r1 = random.random()
                r2 = random.random()

                A3 = 2 * a * r1 - a
                C3 = 2 * r2

                D_delta = abs(C3 * delta[j] - wolves[i][j])

                X3 = delta[j] - A3 * D_delta

                # New position
                wolves[i][j] = (X1 + X2 + X3) / 3

                # Keep within bounds
                wolves[i][j] = max(
                    lower_bound,
                    min(upper_bound, wolves[i][j])
                )

        # Print every 100 iterations
        if (iteration + 1) % 100 == 0:

            print(
                "Iteration",
                iteration + 1,
                ": Best fitness =",
                format(alpha_fitness, ".4f")
            )

    # Step 8: Return best solution
    return alpha, alpha_fitness


# Main program
best_solution, best_fitness = gwo()


print("\nOptimization completed!")
print(
    "Best solution =",
    [
        format(best_solution[0], ".8e"),
        format(best_solution[1], ".8e")
    ]
)

print(
    "Minimum objective value =",
    format(best_fitness, ".8e")
)
