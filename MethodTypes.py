#Instance Methods -- ( self )based on Object
#class Methods -- ( cls ) can call using class name
#Static Methods --
class Methods:
    school = "University of New Haven"
    def __init__(self,m1, m2):
        self.m1 = m1
        self.m2 = m2

    def avg(self):
        return (self.m1+self.m2)/2

    @classmethod
    def sname(cls):
        print("school: ",cls.school)

    @staticmethod
    def stat():
        print("Static Method")



mth1 = Methods(10,20)
mth2 = Methods(20,30)

print("mth1.avg():",mth1.avg())
print("mth2.avg():",mth1.avg())

Methods.stat()
Methods.sname()

mth1.stat()
mth1.sname()

mth2.stat()
mth2.sname()