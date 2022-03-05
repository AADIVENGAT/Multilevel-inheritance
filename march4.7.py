#multilevel inheritance:
class A:
    def __init__(self):
        print("A init")
    def feature_1(self):
        print("Feature 1")
    def feature_2(self):
        print("Feature 2")        

class B:
    def __init__(self):
        print("B init")
    def feature_3(self):
        print("Feature 3")
    def feature_4(self):
        print("Feature 4")   

class C(A,B):
    def feature_5(self):
        print("Feature 5")
    def feature_6(self):
        print("Feature 6")     

c1=C()   
c1.feature_5()     
c1.feature_6()                      