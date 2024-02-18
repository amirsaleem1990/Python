import requests
from bs4 import BeautifulSoup
import re
import pickle
import os

pattern = "^"
urls = open("f_.txt", "r").read().splitlines()
files = os.listdir("thumbs")
def func_(url):
	if str(urls.index(url))+".pkl" in files:
		print("------------ Alreadey completed")
		return None
	e = urls.index(url)
	print(e)
	s = BeautifulSoup(requests.get(url).text, "lxml")
	x2= s.find_all('a', href=re.compile(pattern))
	try:
		thumb = s.find("meta", {"property" : "og:image"}).get('content')
		pickle.dump(thumb, open(f"thumbs/{e}.pkl", 'wb'))
	except:
		print(f"{e} ----------------------- FAILED")



from multiprocessing import Pool
pool = Pool()   # Create a multiprocessing Pool
pool.map(func_, urls)