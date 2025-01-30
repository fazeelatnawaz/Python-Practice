continents = "France is in {} China is in {}".format("Europe","Asia")
print(continents)

squares ="{0} times {0} equals {1}". format(3,9)
print(squares)

population = "{name}'s population is {pop} million"  .format(name="Brazil", pop=209)
print(population)

two_decimaL_place = "I own{:.2f}% of the company".format(32.5548651132)
print(two_decimaL_place)

india_pop = "The approx pop of {} is {:,}" .format("India", 1234000000)
print(india_pop)

balance_string = "your bank balance is ${:,.2f}" .format(12345.678)
print(balance_string)