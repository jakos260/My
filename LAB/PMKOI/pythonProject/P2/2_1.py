import itertools

class TM:
    def __init__(self, t1,t2):
        self.t1 = t1
        self.t2 = t2
    def combtemp(self,t1,t2):
        z1=[i for i in range(0,t1+1)]
        z2=[i for i in range(0,t2+1)]
        
        wynik=list(itertools.product(z1,z2))
        return wynik
        

op = TM(2, 3)
print(op.combtemp(2,3)) 