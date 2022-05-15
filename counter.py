https://www.youtube.com/watch?v=nKYhDmFtuEk
# Counting Letters
word = "mississippi"
counter = {}
for latter in word:
	if latter not in counter:
		counter[latter] = 0
	counter[latter] += 1
counter
# {'m': 1, 'i': 4, 's': 4, 'p': 2}

# Using .get()
counter = {}
for latter in word:
	counter[latter] = counter.get(latter, 9) + 1
counter
# {'m': 10, 'i': 13, 's': 13, 'p': 11}


# Using defaultdict
from collections import defaultdict
count = defaultdict(int)
for latter in word:
	counter[latter] += 1
counter
# {'m': 11, 'i': 17, 's': 17, 'p': 13}

from collections import Counter
Counter("mississippi")
# Counter({'m': 1, 'i': 4, 's': 4, 'p': 2})
Counter(list("mississippi"))
# Counter({'m': 1, 'i': 4, 's': 4, 'p': 2})
Counter({"i": 4, "s" : 4, "p":2, "m":1})
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
Counter(i=4, s=4, p=2, m=1)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
Counter(set("mississippi"))
# Counter({'p': 1, 'm': 1, 'i': 1, 's': 1})
Counter(apple=10, orange=15, banana=0, tomato=-15)
# Counter({'apple': 10, 'orange': 15, 'banana': 0, 'tomato': -15})
latters = Counter("mississippi")
latters
# Counter({'m': 1, 'i': 4, 's': 4, 'p': 2})
latters.update("ohio")
latters
# Counter({'m': 1, 'i': 5, 's': 4, 'p': 2, 'o': 2, 'h': 1})
latters.update({"i" : 37, "h" : -5})
latters
# Counter({'m': 1, 'i': 42, 's': 4, 'p': 2, 'o': 2, 'h': -4})

latters.update(s=5, p=5)
latters
# Counter({'m': 1, 'i': 42, 's': 9, 'p': 7, 'o': 2, 'h': -4})

latters["i"]
# 42

for latter in latters:
	print(latter, latters[latter])
# m 1
# i 42
# s 9
# p 7
# o 2
# h -4

latters.keys()
# dict_keys(['m', 'i', 's', 'p', 'o', 'h'])
for latter in latters.keys():
	print(latter, latters[latter])
# m 1
# i 42
# s 9
# p 7
# o 2
# h -4

for count in latters.values():
	print(count)
# 1
# 42
# 9
# 7
# 2
# -4
latters.items()
# dict_items([('m', 1), ('i', 42), ('s', 9), ('p', 7), ('o', 2), ('h', -4)])

for latter, count in latters.items():
	print(latter, count)
# m 1
# i 42
# s 9
# p 7
# o 2
# h -4

latters["a"]
# 0
latters["M"]
# 0

#Most common
sales = Counter(banana=15, tomato=4, apple=38, orange=30)
sales.most_common()
# [('apple', 38), ('orange', 30), ('banana', 15), ('tomato', 4)]

sales.most_common(3) # 3 most common sorted by count
# [('apple', 38), ('orange', 30), ('banana', 15)]

# Least common
sales.most_common(3)[::-1]                     
# [('banana', 15), ('orange', 30), ('apple', 38)]

list(reversed(sales.most_common(3)))           
[('banana', 15), ('orange', 30), ('apple', 38)]

