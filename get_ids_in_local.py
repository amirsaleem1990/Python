#!/usr/bin/python3
"""
Idea ye h k me ksi script ko chalun or us script ki har linke k bad ye line paste kar dun, to har line bad is line k scope me jitny variables hon un ki ids <global_id_dict_.pkl> me save ho jay, taky me ksi dusry terminal sy un ids k throug un variables ki values dekh sakun.
"""
import time
import numpy
import sys
import pickle

global_id_dict_ = {}

def update_all_vars_ids(locals_):
	remove__ = []
	i,str_,z = "","",""
	z = [i for i in locals_ if (not i.startswith("_")) and (not i in ['In', 'Out', 'get_ipython', 'exit', 'quit'])]
	for i in locals_:
		if i in z:
			str_ = str(locals_[i])
			if (str_.startswith("<module")) or (str_.startswith("<function")):
					remove__.append(i)
	z = [i for i in z if not i in remove__]
	return z

for i_id in update_all_vars_ids(locals()): 
	global_id_dict_[i_id] = id(eval(i_id))
	pickle.dump(global_id_dict_, open("global_id_dict_.pkl", "wb"))
print(global_id_dict_)

# ctypes.cast(id_number), ctypes.py_object).value