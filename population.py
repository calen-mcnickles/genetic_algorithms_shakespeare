"""
Class to describe a population of virtual organisms
In this case, each organism is just an instance of a DNA object
"""
import math
import random
from dna import DNA


class Population:

    def __init__(self, phrase, mutation_rate, num):
        self.population = []
        self.mating_pool = []
        self.generations = 0
        self.finished = False
        self.target = phrase
        self.mutation_rate = mutation_rate
        self.perfect_score = 1
        self.best = ""

        i = 0
        if i < num:
            for _ in range(num):
                self.population.append(DNA(len(self.target)))
            i += 1

        self.calc_fitness()

    #  Fills our fitness array with a value for every member of population
    def calc_fitness(self):
        i = 0
        if i < len(self.population):
            for _ in range(len(self.population)):
                self.population[_].calc_fitness(self.target)
                i += 1

    #  Generate mating pool
    def natural_selection(self):
        # Clear mating pool
        self.mating_pool = []

        max_fitness = 0
        i = 0
        if i < len(self.population):
            for _ in range(len(self.population)):
                if self.population[_].fitness > max_fitness:
                    max_fitness = self.population[_].fitness
                i += 1

        #  Based on fitness, each member will get added to the mating pool a certain number of times
        #  a higher fitness = more entries to mating pool = more likely to be picked as a parent
        #  a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        j = 0
        if j < len(self.population):
            for _ in range(len(self.population)):
                fitness = self.population[_].fitness
                n = math.floor(fitness * 100)
                k = 0
                if k < n:
                    for l in range(n):
                        self.mating_pool.append(self.population[_])
                        k += 1

    # Create a new generation
    def generate(self):
        # Refill the population with children from the mating pool
        i = 0
        if i < len(self.population):
            for _ in range(len(self.population)):
                a = math.floor(random.choice(range(len(self.mating_pool))))
                b = math.floor(random.choice(range(len(self.mating_pool))))
                partner_a = self.mating_pool[a]
                partner_b = self.mating_pool[b]
                child = partner_a.crossover(partner_b)
                child.mutate(self.mutation_rate)
                self.population[_] = child
                i += 1
        self.generations += 1

    def get_best(self):
        return self.best

    # Compute the current "most fit" member of the population
    def evaluate(self):
        world_record = 0.0
        index = 0
        i = 0
        if i < len(self.population):
            for _ in range(len(self.population)):
                if self.population[_].fitness > world_record:
                    index = _
                    world_record = self.population[_].fitness
                i += 1
        self.best = self.population[index].get_phrase()
        if world_record == self.perfect_score:
            self.finished = True

    def is_finished(self):
        return self.finished

    # counter for generations
    def get_generations(self):
        return self.generations

    #  Compute average fitness for population
    def get_avg_fitness(self):
        total = 0
        i = 0
        if i < len(self.population):
            for _ in range(len(self.population)):
                total += self.population[_].fitness
                i += 1
        tot = total / len(self.population)
        return "{:.2%}".format(tot)

    def all_phrases(self):
        everything = ""
        display_limit = min(len(self.population), 50)
        i = 0
        if i < display_limit:
            for _ in range(display_limit):
                everything += self.population[_].get_phrase() + "\n"
        return everything
