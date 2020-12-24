# class A(object):
# 	pass

# class B(A):
# 	pass

# class C(A):
# 	pass

# class D(B, C):
# 	pass

# class E(D, A):
# 	pass

# e = E()
# print(E.mro())
# print(E.__mro__)


class A(object):
	pass

class F(object):
	pass

class B(A, F):
	pass

class C(A):
	pass

class D(C):
	pass

class E(C):
	pass

e = E()
print(B.mro())