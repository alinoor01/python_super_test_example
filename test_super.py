
class A(object):
    def __init__(self):
        print("I am from A")

class B(A):
    def __init__(self):
        print("I am from B")
        super().__init__()

class C(A):
    def __init__(self):
        print("I am from C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("I am from D")
        super().__init__()

d = D()

# I am from D
# I am from B
# I am from C
# I am from A


"""
    A
   / ⇖
  B ⇒ C
   ⇖ /
    D

"""