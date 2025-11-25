
class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


# class C(B, A):  # Like this the result would be: b
class C(A, B):
    def c(self):
        self.a()


c = C()
c.c()  # a

print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>,
#  <class '__main__.B'>, <class 'object'>]
