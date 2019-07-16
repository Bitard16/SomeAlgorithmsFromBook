# Quick sort
import random
data = [9,6,4,2,10,11,18,19]
def QuickSort(data):
    if len(data) <= 1:
        return data
    else:
        q = random.choice(data)
        s_data = []
        m = []
        e = []
        for i in data:
            if i < q:
                s_data.append(i)
            elif i> q:
                m.append(i)
            else:
                e.append(i)
        return QuickSort(s_data) + e + QuickSort(m)


print(QuickSort(data))


