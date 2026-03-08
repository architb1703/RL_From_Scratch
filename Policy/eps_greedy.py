import numpy as np

def epsilon_greedy(q_val,eps):
    if(np.random.random()<eps):
        a = np.random.randint(0,2)
    else:
        a = np.argmax(q_val)

    return a