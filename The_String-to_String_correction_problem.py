import numpy as np
import pandas as pd


s1 = 'Saturday'
s2 = 'Sunday'

m = len(s1)
n= len(s2)
D = np.zeros((m+1,n+1))
D[0,:] = list(range(n+1))
D[:,0] = list(range(m+1))

for j in range(1,n+1):
    for i in range(1,m+1):
        if s1[i-1] == s2[j-1]:
            
            D[i,j] = D[i-1,j-1]
        else:
            D[i,j] = np.min([D[i-1,j]+1,D[i,j-1]+1,D[i-1,j-1]+1])
print('Расстояние Левенштейна равно :%i' % D[-1,-1])

print(pd.DataFrame(D,index=list(' '+s1),columns = list(' '+s2)))