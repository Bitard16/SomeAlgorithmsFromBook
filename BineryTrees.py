from bintrees import BinaryTree
import heapq
data = {1:'Kek',2:'Mocha',3:'Prost)',4:'SomeZnach',9:'AlornDance',11:'Kek7'}

tree = BinaryTree(data)
tree.update({6:'Teal'})

def displaySemTree(key,value):
    print('Key :', key,'Значение :', value)

tree.foreach(displaySemTree)

#print(tree.foreach(displaySemTree))

#  Another binery structure

data2 = {1:'Kek',2:'Mocha',3:'Prost)',4:'SomeZnach',9:'AlornDance',11:'Kek7'}

heap = []

for key,value in data.items():
    heapq.heappush(heap,(key,value))
heapq.heappush(heap,(6,'Teallll'))
heap.sort()

for item in heap:
    print('KEy:', item[0],'Znach :',item[1])
print('Element 3 sodershit :', heap[3][1])
print("maks :", heapq.nlargest(1,heap))

