population = [int(n) for n in input().split(", ")]
minimum_wealth = int(input())

if sum(population) / len(population) < minimum_wealth:
    print("No equal distribution possible")

else:
    for i in range(len(population)):
        num = population[i]
        if num < minimum_wealth:
            result = minimum_wealth - num
            max_number = max(population)
            index_max_num = population.index(max_number)
            check_number = max_number - result
            population[i] = minimum_wealth
            population[index_max_num] = check_number
    print(population)
