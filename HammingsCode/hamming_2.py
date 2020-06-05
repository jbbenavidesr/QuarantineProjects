"""
My try at making hammings work. It only works if all the entries are different.

For example, [0.4, 0.3, 0.2, 0.1] will work, [0.6, 0.2, 0.1, 0.1] will not
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math as m

prob = [0.4, 0.3, 0.2, 0.1]

def reduce_list(list_, index):
    """
    Takes a list and returns all the items up to the index, and the sum of all others
    Note to self: [a:b] = [a,b)
    """
    temp = [x for x in sorted(list_[0:index], reverse=True)]
    temp.append(m.fsum(list_[index:]))
    return temp

hamming = {}
done = []
for p in prob:
    hamming[index] = ''

for i in range(1,len(prob)):
    reduced = reduce_list(prob, i)
    reduced_clean = [r for r in reduced if r not in done] # Not sure why this works, but is necessary

    for r in reduced_clean:
        if r in prob:
            if r not in done:
                hamming[str(r)] += '1'
                done.append(r)

            for p in prob:
                if p != r and p not in done:
                    hamming[str(p)] += '0'

print(hamming)