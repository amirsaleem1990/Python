from multiprocessing import Pool
import time
lst = []
a = list(range(50000000))
def process_image(r):
    r = r * r * r
    lst.append(r*r)

start = time.time()
pool = Pool()                         # Create a multiprocessing Pool
pool.map(process_image, a)
end = time.time()
print(end - start)

lst = []
start = time.time()
for i in a:
    process_image(i)
    
end = time.time()
print(end - start)