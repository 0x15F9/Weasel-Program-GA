import unittest
from ga import WeaselProgram

class Test(unittest.TestCase):
    def setUp(self):
        self.target = "HiThere"
        self.population_size = 30
        self.weasel = WeaselProgram(target=self.target, population_size=self.population_size)

    def test_produce_genome(self):
        expected_output = len(self.target)
        obtained_output = len(self.weasel.produce_genome())
        self.assertEqual(obtained_output, expected_output)

    def test_produce_population(self):
        expected_output = self.population_size
        obtained_output = len(self.weasel.produce_population())
        self.assertEqual(obtained_output, expected_output)

    def test_get_fitness(self):
        expected_output = 1
        obtained_output = self.weasel.get_fitness(self.target)
        self.assertEqual(obtained_output, expected_output)

    def test_get_fitness_again(self):
        expected_output = 0
        obtained_output = self.weasel.get_fitness(self.target.swapcase())
        self.assertEqual(obtained_output, expected_output)

    def test_cross_over(self):
        expected_output = len("boycowe")
        obtained_output = len(self.weasel.cross_over("boycott","cowshed" ))
        self.assertEqual(obtained_output, expected_output)

unittest.main()