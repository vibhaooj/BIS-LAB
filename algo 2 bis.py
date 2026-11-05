import random


# Objective / fitness function
def fitness(x):
    return x * x


# Initial particles
particles = [
    {"position": 2.0, "velocity": 0.5},
    {"position": 1.5, "velocity": 0.2},
    {"position": 3.0, "velocity": 0.8},
    {"position": 1.0, "velocity": 0.3}
]


# PSO parameters
w = 0.5          # Inertia weight
c1 = 1.5         # Personal learning factor
c2 = 1.5         # Global learning factor

max_iterations = 3


# Step 3 & 4: Evaluate fitness and initialize pbest
for particle in particles:
    particle["pbest_position"] = particle["position"]
    particle["pbest_fitness"] = fitness(particle["position"])


# Step 5: Find global best
gbest_particle = min(
    particles,
    key=lambda p: p["pbest_fitness"]
)

gbest_position = gbest_particle["pbest_position"]
gbest_fitness = gbest_particle["pbest_fitness"]


# Print initial particles
print("Particle Swarm Optimization")
print("Initial particles:")

for i, particle in enumerate(particles, start=1):
    print(
        "Particle", i,
        ": position =", particle["position"],
        ", velocity =", particle["velocity"]
    )


# PSO iterations
for iteration in range(1, max_iterations + 1):

    # Step 6: Update velocity
    for particle in particles:

        r1 = random.random()
        r2 = random.random()

        particle["velocity"] = (
            w * particle["velocity"]
            + c1 * r1 *
            (particle["pbest_position"] - particle["position"])
            + c2 * r2 *
            (gbest_position - particle["position"])
        )

    # Step 7: Update position
    for particle in particles:
        particle["position"] += particle["velocity"]

    # Step 8: Recalculate fitness
    for particle in particles:

        current_fitness = fitness(
            particle["position"]
        )

        # Update personal best
        if current_fitness < particle["pbest_fitness"]:

            particle["pbest_fitness"] = current_fitness
            particle["pbest_position"] = particle["position"]

    # Step 9: Update global best
    gbest_particle = min(
        particles,
        key=lambda p: p["pbest_fitness"]
    )

    if gbest_particle["pbest_fitness"] < gbest_fitness:

        gbest_fitness = gbest_particle["pbest_fitness"]
        gbest_position = gbest_particle["pbest_position"]

    # Print iteration result
    print(
        "\nIteration", iteration,
        ": Best position =", round(gbest_position, 2)
    )

    print(
        "Best fitness =",
        round(gbest_fitness, 2)
    )


# Final result
print("\nFinal Result:")
print(
    "Global best position =",
    round(gbest_position, 2)
)

print(
    "Minimum fitness value =",
    round(gbest_fitness, 2)
)

print("Optimal solution found!")
