
class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


# class C(A, B):
class C(B, A):
    def c(self):
        self.a()


o = C()
o.c()  # b

import inspect
print(inspect.getmro(C))
# (<class '__main__.C'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class 'object'>)
