# difference between module and papckagas 
import urllib
import urllib.request
type(urllib) 
# <class 'module'>
type(urllib.request) 
# <class 'module'>

# the output of both is <module> so hwo we can identify module from package:
# module is file in HDD
urllib.__path__
# ['/home/home/anaconda3/lib/python3.6/urllib'] 
urllib.request.__paht__
# module 'urllib.request' has no attribute '__paht__'
# -------------------------
# when you ask python to import a module, it starts with the first directory in <sys.path> and checks for an appropriate file. if no match is found in the first directory, it checks the next and so forth until a match is found or python runs out of entries in sys.path in which case an import error is raised. 

eg:
# meri working directory </home/home/Desktop> h, or mujhy 1 file import karni h jo k ksi dusri directory me h, let us say k us ka address </home/home/Downloads/new_file_path/new_module.py> h, is k 2 ways hen, 1- current session k lye, or 2-perminent:
# 1-
import sys
sys.path.append('/home/home/Downloads/new_file_path')
import new_module # ab module import ho jay ga, magar is python k invoirment k khatam hony par ye bhi khatam ho jay ga or agli dafa dubara <sys.path.append....> likhna ho ga.
# 2- 
# open terminal and type:
export PYTHONPATH="you_module_path"
# now you perminant saved this module
# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

# -------------------------

