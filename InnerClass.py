class TestInnerClass:

    employerName = "Aon"
    def __init__(self):
        self.domain= self.Domain()

    class Domain:
        def __init__(self):
            self.d1 = "Banking"
            self.d2= "HealthCare"
        def show(self):
            print("d1, d2: ",self.d1,self.d2)

i1 = TestInnerClass()
ic1=i1.Domain()
print("EmployerName:", i1.employerName)
ic1.d1 = "HW"
ic1.d2 = "DC"
ic1.show()

i2 = TestInnerClass()
ic2=i2.Domain()
ic2.show()


