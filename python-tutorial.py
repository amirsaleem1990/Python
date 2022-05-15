You can run a script from the command line using the Python debugger ................ python -m pdb my_script.py .................... It would cause the debugger to stop the execution on the first statement it finds. This s helpful if your script is short. You can then inspect the variables and continue execution line-by-line.

map ........... map(function_to_apply, list_of_inputs)


Most of the times we use lambdas with map so I did the same. Instead of a list of inputs we can even have a list of functions!
def multiply(x):
	return (x*x)
def add(x):
	return (x+x)
funcs = [multiply, add]
for i in range(5):
	value = list(map(lambda x: x(i), funcs))
	print(value)
Output:
[0, 0]
[1, 2]
[4, 4]
[9, 6]
[16, 8]


Reduce is a really useful function for performing some computation on a list and re- turning the result. It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers. So the normal way you might go about doing this task in python is using a basic for loop:
product = 1
list = [1, 2, 3, 4]
for num in list:
	product = product * num
# product = 24

# Now let’s try it with reduce:
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# Output: 24


# Ternary Operators
# tuple Ternary
(if_test_is_false, if_test_is_true)[test]
# Example:
nice = True
personality = ("mean", "nice")[nice]
print("The cat is ", personality)
# Output: The cat is nice

This works simply because True == 1 and False == 0, and so can be done with lists in addition to tuples.
The above example is not widely used and is generally disliked by Pythonistas for not being Pythonic. It is also easy to confuse where to put the true value and where to put the false value in the tuple.
Another reason to avoid using a tupled ternery is that it results in both elements of the tuple being evaluated, whereas the if-else ternary operator does not.
# Example:
condition = True
print(2 if condition else 1/0)
#Output is 2
print((1/0, 2)[condition])
#ZeroDivisionError is raised

This happens because with the tupled ternary technique, the tuple is first built, then an index is found. For the if-else ternary operator, it follows the normal if-else logic tree. Thus, if one case could raise an exception based on the condition, or if either case is a computation-heavy method, using tuples is best avoided.

# ShortHand Ternary
In python there is also the shorthand ternary tag which is a shorter version of the normal ternary operator you have seen above.
Syntax was introduced in Python 2.5 and can be used in python 2.5 or greater.
# Example
>>> True or "Some"
True
>>>
>>> False or "Some"
'Some'
The first statement (True or “Some”) will return True and the second statement (False or “Some”) will return Some.
This is helpful in case where you quickly want to check for the output of a function and give a useful message if the output is empty:
>>> output = None
>>> msg = output or "No data returned"
>>> print(msg)
No data returned

Or as a simple way to define function parameters with dynamic default values:
>>> def my_function(real_name, optional_display_name=None):
>>>
optional_display_name = optional_display_name or real_name
>>>
print(optional_display_name)
>>> my_function("John")
John
>>> my_function("Mike", "anonymous123")
anonymous123





3.7.3 Returning functions from within functions:
It is not necessary to execute a function within another function, we can return it as an output as well:
def hi(name="yasoob"):
	def greet():
		return "now you are in the greet() function"
	def welcome():
		return "now you are in the welcome() function"
	if name == "yasoob":
		return greet
	else:
		return welcome
a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>
#This clearly shows that `a` now points to the greet() function in hi()
#Now try this
print(a())
#outputs: now you are in the greet() function



