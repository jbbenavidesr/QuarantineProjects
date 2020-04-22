p1 = [0.81, 0.09, 0.09, 0.01]
p2 = [0.64, 0.16, 0.16, 0.04]
p3 = [0.45, 0.35, 0.1, 0.05, 0.05]

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

print(hamming(p3))