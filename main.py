"""
Inspired by ->
Genetic Algorithm, Evolving Shakespeare
The Coding Train / Daniel Shiffman
https://thecodingtrain.com/more/archive/nature-of-code/9-genetic-algorithms/9.4-looking-at-code.html

Demonstration of using a genetic algorithm to perform a search

setup()
 # Step 1: The Population
   # Create an empty population (an array or ArrayList)
   # Fill it with DNA encoded objects (pick random values to start)

draw()
 # Step 1: Selection
   # Create an empty mating pool (an empty ArrayList)
   # For every member of the population, evaluate its fitness based on some criteria / function,
     and add it to the mating pool in a manner consistent with its fitness, i.e. the more fit it
     is the more times it appears in the mating pool, in order to be more likely picked for reproduction.

 # Step 2: Reproduction Create a new empty population
   # Fill the new population by executing the following steps:
      1. Pick two "parent" objects from the mating pool.
      2. Crossover -- create a "child" object by mating these two parents.
      3. Mutation -- mutate the child's DNA based on a given probability.
      4. Add the child object to the new population.
   # Replace the old population with the new population

  # Rinse and repeat
"""

from population import Population as p
from time import time


def setup():
    target = "My first genetic algorithm project."
    mutation_rate = 0.01
    popmax = 1000

    new_pop = p(target, mutation_rate, popmax)
    return new_pop


# create population
pop = setup()
start_time = time()

done = False
while not done:
    #  Generate mating pool
    p.natural_selection(pop)

    #  Create next generation
    p.generate(pop)
    print(p.all_phrases(pop))

    #  Calculate fitness
    p.calc_fitness(pop)
    print(f"Current generation: {p.get_generations(pop)}")
    print(f"Average fitness score: {p.get_avg_fitness(pop)}")

    p.evaluate(pop)
    print(f"Best phrase: {p.get_best(pop)}")
    in_sec = "{:.2f}".format((time() - start_time))
    print(f"Runtime: {in_sec} seconds")

    #  If we found the target phrase, stop
    if p.is_finished(pop):
        done = True
