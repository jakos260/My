import time
import numpy as np

start1 = time.time()

li = [i for i in range(1000000)]
li_new = [li[i]*li[i] for i in range(len(li))]

end1 = time.time()
print('czas list', (end1-start1))

start2 = time.time()

tab = np.arange(0,1000000)
tab_new = np.multiply(tab, tab)

end2 = time.time()
print('czas tabeli', (end2-start2))







