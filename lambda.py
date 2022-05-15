# The lambda function is an expression, not a statement: the def statement assigns the new function to the name in the header, 
#      the lambda function returns it as a result. Remember: lambda returns a value (a new function).
# The body of a lambda function is an expression, not a block of statements: the lambda expression body (f) can be thought 
#      of as the return statement in a standard function with the def statement. For this reason, the lambda function is also
#      less general because its body is limited to a single expression, without useful logic statements (if, for…).


calculator = {
	"add"      : (lambda x,y : f"add function called.      {x}+{y} = {x+y}"),
	"subtract" : (lambda x,y : f"subtract function called. {x}-{y} = {x-y}"),
	"multiply" : (lambda x,y : f"multiply function called. {x}*{y} = {x*y}"),
	"devide"   : (lambda x,y : f"devide function called.   {x}/{y} = {x/y}") 
}

x,y = 3,4

calculator['add'](x,y)        # add function called.      3+4 = 7
calculator['subtract'](x,y)   # subtract function called. 3-4 = -1
calculator['multiply'](x,y)   # multiply function called. 3*4 = 12
calculator['devide'](x,y)     # devide function called.   3/4 = 0.75


############################################

# set default values fro lambda perameters
q = lambda x=3: x**2
q()  # 9
q(5) # 25


############################################

greetings = lambda time: print("Good morning") if time < 15 else print("Good Evening")

greetings(11) # Good morning
greetings(17) # Good Evening


import sys
talk = lambda x:list(map(sys.stdout.write, x))
words1 = ["I",  "love",  "TTML"]
words2 = ["I ",  "love ",  "TTML"]

talk(words1) # IloveTTML[1, 4, 4]
talk(words2) # I love TTML[2, 5, 4]



