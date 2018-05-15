import string
from random import choice, uniform

class WeaselProgram:

    def __init__(self, target="HelloWorld", population_size=25):
        self.target          = target
        self.population_size = population_size
        self.pool            = list(string.ascii_letters)
        self.population      = self.produce_population()

    def produce_genome(self):
        genome = []
        while len(genome) != len(self.target):
            genome.append(choice(self.pool))
        return ''.join(genome)

    def produce_population(self):
        return [self.produce_genome() for i in range(self.population_size)]

    def regenerate_population(self, previous_population):
        """ Regenerates population using part of previous population and part of new population """
        new_population = []
        threshold_value = ( self.population_size // 5 ) * 6 # 5/6 of the previous population will be renewed
        for i in range(threshold_value):
            new_population.append(self.cross_over())
        for i in range(threshold_value, self.population_size):
            new_population.append(self.produce_genome)
        self.population = new_population
        return new_population

    def get_fitness(self, genome):
        f = 0.0
        for i in range(len(self.target)):
            if genome[i] == self.target[i]:
                f += 1
        # fitness is between 0 and 1
        return float(f / len(self.target))

    def cross_over(self):
        father_genome = self.select_parent()
        mother_genome = self.select_parent()
        child_genome = []
        for i in range(len(self.target)):
            c = choice([0, 1])
            if c == 0:
                child_genome.append(father_genome[i])
            else:
                child_genome.append(mother_genome[i])
        return ''.join(child_genome)

    def select_parent(self):
        max     = sum([self.get_fitness(c) for c in self.population])
        pick    = uniform(0, max)
        current = 0
        for chromosome in self.population:
            current += self.get_fitness(chromosome)
            if current > pick:
                return chromosome

    def intermediary_result(self):
        result = []
        for genome in self.population:
            result.append({
                'genome': genome,
                'fitness': self.get_fitness(genome)
            })
        return result

        