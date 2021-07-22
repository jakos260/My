
import numpy as np

m1 = np.random.normal(50,20,size=(7,7))
m2 = m1.astype(int)
print(m1)
print(m2)

v_wlasne = np.linalg.eigvals(m2)
w_wlasne = np.linalg.eig(m2)
print('wartosci wlasne', v_wlasne)
print('wektory wlasne', w_wlasne)

m2_odwr = np.linalg.inv(m2)
print('macierz odwrotna', m2_odwr)

v = [1,2,3,4,5,6,7]
m2_mul = np.dot(m2,v)
print('macierz pomnożona', m2_mul)

a = m2.diagonal()
print('główna przekątna do kwadratu', (a*a))

v_os = np.linalg.svd(m2)
print('wartośći osobliwe', v_os)