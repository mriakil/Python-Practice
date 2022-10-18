
class A:

    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:

    def __init__(self):
        print("in B Init")
    def feature1(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(B,A):

    def __init__(self):
        super().__init__()
        print("in C Init")

    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")

    def feat(self):
        super().feature1()

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature1()


c1 = C()

c1.feature1()
c1.feature4()
c1.feature5()

c1.feat()

