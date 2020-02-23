import numpy as np

values = np.array([3,4,3,5,8,10])
weights = np.array([2,3,4,4,5,9])
items = len(weights)
capacity = 20

memo = dict()

for size in range(0,capacity+1,1):
    memo[(-1,size)] = ([],0)
    
for item in range(items):
    for size in range(0,capacity+1,1):
        # Если предемет не помещается в рюкзак
        if weights[item] > size:
            memo[item,size] = memo[item-1,size]
        else:
            #Если предмет помещается в рюкзаке ищем лучше
            # решение для остального пространства рюкзака
            previous_row,previous_row_value = memo[item-1,size-weights[item]]
            if memo [item-1,size][1] > values[item] + previous_row_value:
                memo[item,size] = memo[item-1,size]
            else:
                memo[item,size] = (previous_row + [item],previous_row_value+values[item])

best_set,score = memo[items-1,capacity]

print(best_set,score)

print(len(memo))

from scipy.special import comb

objects = 6

print(np.sum([comb(objects,k+1) for k in range(objects)]))
                                                                        
