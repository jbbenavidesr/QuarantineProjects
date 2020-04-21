p = [0.81, 0.09, 0.09, 0.01]


def hamming(probabilities):
    probabilities.sort(reverse=True)
    order= [str(i) for i in range(len(probabilities))]

    return list(zip(probabilities, order))

print(hamming(p))