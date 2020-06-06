import itertools
import math as m

def entropy(probabilities):
    """
    Returns the entropy of a system, given the probabilities of each possible state.
    """
    S=0
    for p in probabilities:
        I = -m.log2(p)
        S += p*I
    return S

def group_probabilities(prob, N):
    """
    Return the probabilities of the different combinations that result from sending 
    the messages in groups of N.
    """
    comb = itertools.product(prob, repeat=N)
    g_prob = []

    for i in comb:
        product = 1
        for j in i:
            product *= j 
        g_prob.append(product)

    return tuple(g_prob)    

def get_history(probabilities):
    """ 
    Returns tuple with a history of the position occupied by a given probability
    in the process of adding the last 2 and reducing the list to only 2 
    possibilities
    """

    history = [str(i) for i in range(len(probabilities))]
    last = probabilities[-1] + probabilities[-2]
    values = [probabilities[i] for i in range(len(probabilities)-2)] + [last]
    while len(values) >= 2:
        values.sort(reverse=True)
        if last == values[-1]:
            for i in range(len(values)):
                history[i] += str(i)

            for i in range(len(values), len(probabilities)):
                history[i] += str(len(values)-1)

        else: 
            ind = values.index(last)
            for i in range(ind):
                history[i] += str(i)

            for i in range(len(values)-1, len(probabilities)):
                history[i] += str(ind)

            for i in range(ind, len(values)-1):
                history[i] += str(i+1)

        last = values[-1] + values[-2]
        values = [values[i] for i in range(len(values)-2)] + [last]
    
    return tuple(history)


def hamming(probabilities):
    """ 
    Returns the Hamming code given a list with the probabilities of some given inputs
    to be sent.
    """

    probabilities.sort(reverse=True)
    history = get_history(probabilities)

    hamming = ['' for h in history]

    for j in range(len(history)):
        for i in range(len(history[0])):
            if history[j][-(i+1)] == str(i):
                hamming[j] += '0'
            elif history[j][-(i+1)] == str(i+1):
                hamming[j] += '1'

            
    return tuple(zip(probabilities, hamming))

def average_length(probabilities, N=1):
    """
    Gets the average length of the messages using the Hamming Code
    """
    code = hamming(list(probabilities))
    L = 0

    for p, c in code:
        L += p * len(c)

    return L

p = [0.8,0.2]

if __name__ == '__main__':
    print(sorted(list(group_probabilities(p,3)), reverse=True))
