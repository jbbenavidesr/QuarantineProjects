p = [0.81, 0.09, 0.09, 0.01]


def hamming(probabilities):
    probabilities.sort(reverse=True)
    order = [str(i) for i in range(len(probabilities))]
    last = probabilities[-1] + probabilities[-2]
    values = [probabilities[i] for i in range(len(probabilities)-2)] + [last]
    while len(values) >= 2:
        values.sort()
        if last == values[-1]:
            for i in range(len(values)):
                order[i] += str(i)

            for i in range(len(values), len(probabilities)):
                order[i] += str(len(values)-1)

        else: 
            ind = values.index(last)
            for i in range(ind):
                order[i] += str(i)

            for i in range(len(values)-1, len(probabilities)):
                order[i] += str(ind)

            for i in range(ind, len(values)-1):
                order[i] += str(i+1)
                
        last = values[-1] + values[-2]
        values = [values[i] for i in range(len(values)-2)] + [last]
            
    return list(zip(probabilities, order))

print(hamming(p))