import inspect
def retrieve_name(var):
    """ This function take a variable name, and return that name as a string"""
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]




a,b,c = 1,2,3
for i in [a,b,c]:
    print(retrieve_name(i)[0])

