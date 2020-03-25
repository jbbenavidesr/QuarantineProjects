p = [0.8, 0.2]

def combined(N, probabilities):
    combined = []
    for i in range(N):
        for j in range(N):
            combined.append(probabilities[i]*probabilities[j])
    return combined

def hamming(probabilities):
    return ['1','0']

print(combined(2, p))
# print(hamming(p))