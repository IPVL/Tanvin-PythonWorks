#! /usr/bin/env python
class A(object):
	def foo(self):
 		print("class A")

class B(object):
 	def foo(self):
 		print("class B")

class C(A):
 	pass

class D(B):
 	def foo(self):
 		print("class D")

class E(A):
 	def foo(self):
 		print("class E")

# # # this gives: Cannot create a consistent method resolution order (MRO) for bases E, A
class F(D, A, E):
	pass

# # # this gives: Cannot create a consistent method resolution order (MRO) for bases E, A
# # class F(A, E):
# # 	pass

# # search order: F, C, D, B, E, A, object
# class F(C, D, E):
# 	pass

F().foo()
print type.mro(type(F()))

