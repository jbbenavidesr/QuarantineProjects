p1 = [0.81, 0.09, 0.09, 0.01]
p2 = [0.64, 0.16, 0.16, 0.04]
p3 = [0.45, 0.35, 0.1, 0.05, 0.05]

def get_history(probabilities):

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
    
    return history


def hamming(probabilities):
    probabilities.sort(reverse=True)
    history = get_history(probabilities)
            
    return list(zip(probabilities, history))

print(hamming(p1))