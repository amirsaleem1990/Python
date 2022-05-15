def a_new_decorator(a_func):
	def wrap_the_function():
		print("A decorator called")
		import time
		s = time.time()
		a_func()
		e = time.time()
		print(e-s, "Time consumed")
	return wrap_the_function

@a_new_decorator
def a_function_require_decoration():
	print("An Orignal function called")

a_function_require_decoration()