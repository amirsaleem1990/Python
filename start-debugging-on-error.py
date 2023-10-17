import os
import sys
import pdb

# os.environ['PYTHONBREAKPOINT'] = 'pdb.post_mortem'

def my_excepthook(type, value, traceback):
    # pdb.post_mortem()
    pdb.set_trace()

sys.excepthook = my_excepthook

def divide(a, b):
    x = 44
    return a / b
x = 33
result = divide(5, 0)
print(result)

