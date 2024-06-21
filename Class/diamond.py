# Ромбовидне успадкування
# Method resolution order(MRO)

class A:
    def hi(self):
        print('A')


class B(A):
    def hi_(self):
        print('B')


class C(A):
    def hi_(self):
        print('C')


class D(B, C):
    def hi_(self):
        print(55)


d = D()
d.hi()
