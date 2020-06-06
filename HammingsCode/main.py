import matplotlib.pyplot as plt
import hamming as ham

Nmax= 5
p = [0.8, 0.2]

data=[]

for n in range(1, Nmax):
    l = ham.average_length(ham.group_probabilities(p, n), n)
    data.append(l)

plt.plot(data)
plt.show()