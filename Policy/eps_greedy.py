import numpy as np
import random

def epsilon_greedy(q_val,eps):
    if(random.random()<eps):
        a = random.randint(0,1)
    else:
        a = np.argmax(q_val)

    return a