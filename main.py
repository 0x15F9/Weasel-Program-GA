from ga import WeaselProgram

def get_highest_fitness_per_population(list_dict):
    list_fitness = [x['fitness'] for x in list_dict]
    max_fitness = max(list_fitness)
    for res in list_dict:
        if res['fitness'] == max_fitness:
            print(res)
    print('')
    return max_fitness 

def main():
    wp = WeaselProgram(population_size=100)
    max = get_highest_fitness_per_population(wp.intermediary_result())
    while max != 1:
        wp.regenerate_population(wp.population)
        max = get_highest_fitness_per_population(wp.intermediary_result())
main()