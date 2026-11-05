import random


# Distance matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
n = len(distance)

# ACO parameters
num_ants = 10
alpha = 1          # Pheromone importance
beta = 2           # Distance importance
evaporation = 0.5
Q = 100
iterations = 100


# Calculate length of a tour
def tour_distance(tour):
    total = 0

    for i in range(n - 1):
        total += distance[tour[i]][tour[i + 1]]

    # Return to starting city
    total += distance[tour[-1]][tour[0]]

    return total


# Select next city based on probability
def select_next_city(current_city, unvisited, pheromone):

    probabilities = []

    for city in unvisited:

        pheromone_value = pheromone[current_city][city] ** alpha

        distance_value = (1 / distance[current_city][city]) ** beta

        probability = pheromone_value * distance_value

        probabilities.append(probability)

    # Calculate total probability
    total = sum(probabilities)

    probabilities = [
        p / total for p in probabilities
    ]

    # Select city using probability
    return random.choices(
        list(unvisited),
        weights=probabilities,
        k=1
    )[0]


# Ant Colony Optimization
def ant_colony_optimization():

    # Step 1: Initialize pheromone matrix
    pheromone = [
        [1.0 for _ in range(n)]
        for _ in range(n)
    ]

    # Store best tour
    best_tour = None
    best_distance = float("inf")

    # Step 2: Iterations
    for iteration in range(iterations):

        all_tours = []

        # Step 3: Each ant constructs a tour
        for ant in range(num_ants):

            # Select starting city
            start_city = random.randint(0, n - 1)

            tour = [start_city]

            unvisited = set(range(n))
            unvisited.remove(start_city)

            # Visit all cities
            while unvisited:

                current_city = tour[-1]

                next_city = select_next_city(
                    current_city,
                    unvisited,
                    pheromone
                )

                tour.append(next_city)
                unvisited.remove(next_city)

            # Calculate tour distance
            total_distance = tour_distance(tour)

            all_tours.append(
                (tour, total_distance)
            )

            # Update best tour
            if total_distance < best_distance:

                best_distance = total_distance
                best_tour = tour.copy()

        # Step 4: Evaporate pheromone
        for i in range(n):
            for j in range(n):

                pheromone[i][j] *= (1 - evaporation)

        # Step 5: Deposit new pheromone
        for tour, total_distance in all_tours:

            pheromone_amount = Q / total_distance

            for i in range(n - 1):

                city1 = tour[i]
                city2 = tour[i + 1]

                pheromone[city1][city2] += pheromone_amount
                pheromone[city2][city1] += pheromone_amount

            # Return edge
            city1 = tour[-1]
            city2 = tour[0]

            pheromone[city1][city2] += pheromone_amount
            pheromone[city2][city1] += pheromone_amount

        # Print progress
        if (iteration + 1) % 10 == 0:

            print(
                "Iteration",
                iteration + 1,
                ": Best distance =",
                best_distance
            )

    return best_tour, best_distance


# Main program
best_tour, best_distance = ant_colony_optimization()


# Convert city numbers from 0-based to 1-based
best_tour_display = [
    city + 1 for city in best_tour
]

# Add starting city at the end
best_tour_display.append(best_tour_display[0])


print("\n----- Ant Colony Optimization Results -----")

print(
    "Best tour:",
    " -> ".join(map(str, best_tour_display))
)

print(
    "Minimum distance:",
    best_distance
)
