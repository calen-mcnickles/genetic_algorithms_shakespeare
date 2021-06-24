"""
A class to describe a pseudo-DNA, id genotype
Functionality:
- Converts DNA into a string
- calculate  DNA's Fitness
- mate DNA with another set of DNA
- mutate DNA

"""
import math
import random


def new_char():
    c = math.floor(random.randint(63, 122))
    if c == 63:  # allows us to get space
        c = 32
    if c == 64:  # allows us to get "."
        c = 46
    return chr(c)


#  Creates random DNA
class DNA:

    def __init__(self, num):
        self.genes = []
        self.fitness = 0
        i = 0
        if i < num:
            for _ in range(num):
                self.genes.append(new_char())
                i += 1

    # Converts char array to string
    def get_phrase(self):
        return ''.join(self.genes)

    # Fitness function (returns floating point percentage of "correct" characters)
    def calc_fitness(self, target):
        """Iterates through gene chars and compares char at each index to target char at same index.
        Then it returns a % of correct chars"""
        score = 0
        i = 0
        if i < len(self.genes):
            for _ in range(len(self.genes)):
                if self.genes[_] == target[_]:
                    score += 1
                i += 1
        self.fitness = score / len(target)


    # Crossover
    def crossover(self, partner):
        # A new child
        child = DNA(len(self.genes))
        midpoint = math.floor(random.randrange(0, len(self.genes)))

        i = 0
        if i < len(self.genes):
            for _ in range(len(self.genes)):
                if i > midpoint:
                    child.genes[_] = self.genes[_]
                    i += 1
                else:
                    child.genes[_] = partner.genes[_]
                    i += 1
        return child

    #  Based on mutation probability, picks a new random character
    def mutate(self, mutation_rate):
        i = 0
        if i < len(self.genes):
            for _ in range(len(self.genes)):
                if random.random() < mutation_rate:
                    self.genes[_] = new_char()
                i += 1
