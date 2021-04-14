class TM:
    def __init__(self, t1,t2):
        self.t1 = t1
        self.t2 = t2
    def combtemp(self,t1,t2):
        wynik = []
        for i in range(0,t1+1):
            for j in range(0,t2+1):
                a.append((i,j))
        
        return a
        

op = TM(2, 3)
print(op.combtemp(2,3)) 