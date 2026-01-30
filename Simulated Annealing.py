import random
import math

def simulated_annealing():
    current = 10
    temp = 100

    while temp > 1:
        next_state = current + random.randint(-1,1)
        if next_state < current:
            current = next_state
        temp *= 0.9

    print("Final State:", current)

simulated_annealing()
