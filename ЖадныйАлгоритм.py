

def change(to_be_changed,demomination):
    resulting_change = list()
    for bill in demomination:
        while to_be_changed >= bill:
            resulting_change.append(bill)
            to_be_changed = to_be_changed - bill
    return resulting_change,len(resulting_change)

currency = [100,50,20,10,5,1]
amount = 1004
print(change(amount,currency))


from heapq import heappush,heappop,heapify
from collections import defaultdict , Counter
from random import shuffle,seed
generator = ["A"]*6+["C"]*4+["G"]*2+["T"]*2
text = ""
seed(4) # Позволяет одинаковые рандомные чилса выдавать
for i in range(1000):
    shuffle(generator) # Перемешивает случайно список
    text += generator[0]

print(text)
frequencies = Counter(list(text))
print(frequencies)

heap = ([[freq,[char,""]] for char,freq in frequencies.items()])
heapify(heap)
print(heap)

iteration = 0
while len(heap) > 1:
    iteration +=1
    io = heappop(heap)
    hi = heappop(heap)
    #print('Шаг %i первый: :s второй:%s' % (iteration,io,hi))
    for pair in io[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heappush(heap,[io[0]+ hi[0]] + io[1:] + hi[1:])



tree = sorted(heappop(heap)[1:],key=lambda p: (len(p[-1]),p))
print("Символ\tВес\tКод")
for e in tree:
    print("%s\t%s\t%s" % (e[0], frequencies[e[0]],e[1]))