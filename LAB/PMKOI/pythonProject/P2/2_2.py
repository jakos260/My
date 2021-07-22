class meas:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
   
    def __repr__(self):
        return (self.p1+ ' ' +self.p2)
        
        
        
m1 = meas("Pomiar", "Temperatury")
m2 = meas("Pomiar", "Rezystancji")
m3 = meas("Pomiar", "pH")
mlist = [m1, m2, m3]
print(mlist)
