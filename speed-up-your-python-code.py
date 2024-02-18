# First off: optimizing usually is not your primary concern, writing readable code is.
    # Premature optimization is the root of all evil. (Donald Knuth)

# Start with going through PythonSpeed/PerformanceTips
# Now do some profiling
# Don't optimize what isn't slowing you down.
# Then based on what the bottlenecks are, you can try one or more of the following things:
# Identify 'hot' parts of your code. These are functions which end up taking large chunks of time or are executed many times (typically function calls inside loops).
# Identify whether most of your time is spent waiting for disk I/O or actual computation. If the code is I/O intensive, you can't do much with your code. Try using better storage formats or in-memory caching.

# Builtin functions like map are implemented in C code. So the interpreter doesn't have to execute the loop, this gives a considerable speedup

# Python is less good at using threads to improve performance on multi-threading machines, but that's probably less of an issue now, when we often scale up by getting more CPUs on the cloud.

# If you add Python 3 (PEP-484) type annotations for strategic variables, you can usually make it run at C speed.

# you don’t have to worry about writing C subroutines. But still if you want ,C part in python would cover CPU bound tasks i.e heavy tasks that crunch CPU for calculations.The reason is for CPU bound tasks if run through normal Python ,there would be problem of GIT(Global Interpreter Lock ) and code will slow down for sure. So here comes C for rescue.

# Learn how to link in compiled C and C++ code. When you profile your program you will probably find that 90% or more of the time is spent in just one subroutine. Re-code that subroutine in C or C++. Also try to use compiled, linked-in libraries rather than those written in native Python.

# multi-threading is serialized in Python due to its GIL 

# Benchmark
    # Test various alternatives of the portions you still find to run too slowly. Sometimes it's not as obvious as it could be. Sometimes a particular data structure runs faster even though its complexity is higher. E.g. searching in O(N) through an array may be faster than a hash table if they're both short, thus making the extra time needed to build the hash table and calculate hash codes nullify the N(1) gain. This is very situation specific, thus you need to benchmark with real-world data to try and find out how it will actually perform "in-the-wild"

# Write idiomatic code:
    # This may sound counter-intuitive but writing idiomatic code will make your code faster in most cases. This is because Python was designed to have only one obvious/correct way to do a task ("There should be one-- and preferably only one --obvious way to do it." - The Zen of Python).

# Some data structures inherently cause extra complexity, e.g. obtaining the nth item in a linked list means the DS steps through all N items from the first to the nth. Others may reduce complexity greatly, e.g. searching for an item in an array is O(N), but searching for the same in a BST is O(log N) and searching though a hashtable is O(1). So use the DS which is most appropriate for the task at hand and also has the least complexity.

Python it usually means the most obvious way is better e.g. 
    x+x
    # is faster than 
    x*2
    # or even 
    X<<1

    # Note: It's seems wrong:
    %%timeit 
    c = 0 
    while c < 300:  
        c += 1 
        x*x 
    # 16.7 µs ± 77.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

    %%timeit 
    c = 0 
    while c < 300:  
        c += 1 
        x+x 
    # 16.9 µs ± 415 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)




# Python is also very slow at resolving function addresses. So if you are going to access a method often (inside a loop) consider remapping it to a variable.
    myfunc = myObj.func 
    for i in range(n): 
        myfunc(i) # faster than myObj.func(i) 


# How to spot performance issues?
# python -m cProfile [-o output_file] [-s sort_order] myscript.py
# python -m cProfile my_code.py 

# use sets for getting common vales:
    %%timeit 
    set(a) & set(b)
    # 584 ns ± 4.11 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    %%timeit
    [i for i in a if i in b]
    # 905 ns ± 10.2 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# If you feel the need for speed, go for built-in functions – you can’t beat a loop written in C. Check the library manual for a built-in function that does what you want

    # BUT In the following list comprehention is much faster then built-in 'filter'
    # ipython3 7.26.0

    items = ['chair', 'apple', 'water', 'table', 'orange']
    fruits = ['apple', 'orange', 'grape']

    %%timeit
    list(filter(lambda x:x in items, fruits))
    # 596 ns ± 4.24 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

    %%timeit
    [i for i in items if i in fruits]
    # 444 ns ± 8.27 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)





# generators result in the lazy (on demand) generation of values, which translates to lower memory usage. Good news is that in Python 3 range, d.items() etc return generators (in Python 2 use xrange, d.iteritems() respectively). Another good reason to switch to Python 3 🙂

# __slots__ (https://docs.python.org/2/reference/datamodel.html): 
    # ‘the __slots__ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because __dict__ is not created for each instance’, so this is really useful if you have a lot of instances (here (http://tech.oyster.com/save-ram-with-python-slots/) is a real-world example).

# ‘if variable:’ is faster than the un-idiomatic ‘if variable == True:’ 

# ‘value in set(list)’  is actually expensive because you have to do the list-to-set cast. The suggested set(a) & set(b) instead of double-for-loop has this same problem.

# Measure which parts of your code take the most time to run. Focus on those parts first.

# Proper algorithm & data structure 
#     Each data structure has a significant effect on runtime. There are many built-in data structures such as list, tuple, set, and dictionary in python. Most of the people use list data structure in all the cases.

#     In python, sets and dictionaries have O(1) lookup performance as they use hash tables for that. You can use sets and dictionaries instead of lists in the following cases:

#         You do not have duplicate items in the collection.
#         You need to search items repeatedly in the collection.
#         The collection contains a large number of items. 
    # As an example, say we are crunching millions of numbers and storing the results. We want to create a lookup table that will allow us to quickly see if a value has already been calculated. Speed-wise, the list would be O(n) and the dictionary would be O(1). However, the memory consumption of dictionaries is much larger than lists since it stores a hash table as well. If we are adding new items to the list on the fly, we probably need to use the dictionary. But if we are only using it as a lookup table, it is possible sorting the list and using binary search could be faster depending on the data types. A binary search on a sorted list is O(log n), which will only likely be faster for integer/floating-point data.

# Using built-in functions and libraries
#     Python’s built-in functions are one of the best ways to speed up your code. You must use built-in python functions whenever needed. These built-in functions are well tested and optimized.

#     The reason these built-in functions are fast is that python’s built-in functions, such as min, max, all, map, etc., are implemented in the C language.

#     You should use these built-in functions instead of writing manual functions that will help you execute your code faster.

#     Example:

    newlist = []
    for word in wordlist:
        newlist.append(word.upper())


    # A better way to write this code is:
    newlist = map(str.upper, wordlist)


    # Here we are using the built-in map function, which is written in C. Therefore, it is much faster than using a loop. 


# Use multiple assignments
#     If you want to assign the values of multiple variables, then do not assign them line by line. Python has an elegant and better way to assign multiple variables.

    # Example:
        firstName = "John"
        lastName = "Henry"
        city = "Manchester"
    # A better way to assign these variables is:
        firstName, lastName, city = "John", "Henry", "Manchester"

    # This assignment of variables is much cleaner and elegant than the above one.

# Prefer list comprehension over loops

# Proper import
    # You should avoid importing unnecessary modules and libraries until and unless you need them. You can specify the module name instead of importing the complete library.

    # Importing the unnecessary libraries will result in slowing down your code performance.
    # Example:
    #     Suppose you need to find out the square root of a number. Instead of this:

        import math
        value = math.sqrt(50)
    
        # Use this:

        from math import sqrt
        value = sqrt(50)


    # Do not use dot operation
    #     Try to avoid dot operation. See the below programme.

        import math
        val = math.sqrt(60)

        # Instead of the above style write code like this:

        from math import sqrt
        val = sqrt(60)

        # Because when you call a function using . (dot) it first calls __getattribute()__ or __getattr()__ which then use dictionary operation which costs time. So, try using from module import function.

# String Concatenation     
#     In python, we concatenate strings using the ‘+’ operator. But another way to concatenate the strings in python is using the join method.

#     Join method is a more pythonic way to concatenate strings, and it is also faster than concatenating strings with the ‘+’ operator.

#     The reason why the join() method is faster is that the ‘+’ operator creates a new string and then copies the old string at each step, whereas the join() method does not work that way.

#     Example:

        output = "Programming" + "is" + "fun"
        # Using join method:
        output = " ".join(["Programming" , "is", "fun"])

        # The output of both methods will be the same. The only difference is that the join() method is faster than the ‘+’ operator.

        # NOTE: My (amir saleem) observation is different:
            %%timeit
            new = "This" + "is" + "going" + "to" + "require" + "a" + "new" + "string" + "for" + "every" + "word" 
            # 10.6 ns ± 0.323 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

            %%timeit
            new = " ".join(["This", "will", "only", "create", "one", "string", "and", "we", "can", "add", "spaces."])
            # 207 ns ± 4.09 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

# Use generators

    # If you have a large amount of data in your list and you need to use one data at a time and for once then use generators. It will save you time.
    # It may seem efficient, but it's not

    # See the below code:
        L = []
        for element in set(L):
            # ...
    # The above code may seem efficient because it used set to delete duplicate data. But the reality is that the code is not efficient. Do not forget that converting a list into set takes time. So this code will work better than the previous:
        for element in L:
            ...

# Try a different approach

    # Try new ways to write your code efficiently. See the below code.
    if a_condition:
        if another_condition:
            do_something
    else:
        raise exception

    # Instead of the above code you can write:
    if (not a_condition) or (not another_condition):
        raise exception
    do_something

# Use speed up applications
    # For python's slow speed, some projects have been taken to decrease runtime. Pypy and Numba two of them. In most of the programming contests, you will see pypy if it allows python. These applications will reduce the runtime of your programme.

# Use the latest release of python
    # Python is updated and upgraded regularly, and every release is faster and more optimized. So always use the latest version of python.

    # These were some of the tips to decrease the runtime of python code. There are a few more techniques that you can use. Use a search engine to find those and write efficient code!



# Function Calls Are Expensive
    # Function calls are expensive in Python. While it is often good practice to separate code into functions, there are times where you should be cautious about calling functions from inside of a loop. It is better to iterate inside a function than to iterate and call a function each iteration. Take a look at the following example where we want to create a list of squared values in the range of 1–1,000,000.
    def square(num):
        return num**2
        
    squares = []
    for i in range(1000000):
        squares.append(square(i))
    # Time: 314 ms

    def squares():
      squares = []
      for i in range(1000000):
        squares.append(i**2)
      return squares
    # Time: 245ms

    # We can see that the second method was considerably faster with all things equal other than using a function to square the value. Functions have a lot of overhead, so for simple tasks like this they can add a lot of time relative to the total.



# Lazy Module Importing

#     Traditionally a Python file will import all of the needed libraries at the top. This means that anytime the file is imported or run as a script, all of those libraries are imported. If there are modules that are only needed in certain situations, we don’t necessarily always need to import them. Instead, we can import them only when needed and avoid the overhead of loading them in when they aren’t necessary.

# Take Advantage of Numpy

#     Numpy is a highly optimized library built with C. It is almost always faster to offload math to Numpy rather than relying on the Python interpreter. Numpy also has ultra-efficient data structures designed to hold matrix data that have less overhead than Python’s built-in data structures.

#     If we wanted to square every element in a list, we could do that like this:

    python_list = [i for i in range(1000000)]
    [i**2 for i in python_list]
    # Time: 300ms

    # This works fine, but let’s see how much faster Numpy can do it.
    numpy_array = np.array([i for i in range(1000000)])
    np.square(numpy_array)
    # Time: 602μs

    # Wow! That is much faster than using a list in Python. Numpy opens up all kinds of possibilities for scientific computing with Python. If you work with a lot of matrices, it is well worth becoming a Numpy master. Remember the sum() built-in function from earlier? Using Numpy we can crush its performance as well:

    def builtin_sum():
      return sum(range(10000000))

    def numpy_sum():
      return np.sum(np.arange(0,10000000))
      
    numpy_sum()

    builtin_sum()
    # Time-Builtin: 193ms, Time-Numpy: 22.8ms

    # Numpy can bring incredible performance boosts to math in Python, however, you have to be very careful to stick with Numpy data structures and methods to achieve this level of optimization. Simply creating the array incorrectly in this situation negates the performance boost:

    # This is much slower since "range" is not a numpy function 
    def numpy_sum2():
      return np.sum(np.array(range(1000000)))
      
    numpy_sum2()
    # Time: 952ms
    # This is much slower than simply using built-in Python methods, which is due to time spent converting between Python and Numpy data structures. So, just keep in mind that while Numpy plays well with Python data structures, it is much faster when working solely with Numpy.

    # ---------------------------------------------------
    # Move math to NumPy

    # If you are doing matrix-based or array-based math and you don’t want the Python interpreter getting in the way, use NumPy. By drawing on C libraries for the heavy lifting, NumPy offers faster array processing than native Python. It also stores numerical data more efficiently than Python’s built-in data structures.

    # Relatively unexotic math can be sped up enormously by NumPy, too. The package provides replacements for many common Python math operations, like min and max, that operate many times faster than the Python originals.

    # Another boon with NumPy is more efficient use of memory for large objects, such as lists with millions of items. On the average, large objects like that in NumPy take up around one-fourth of the memory required if they were expressed in conventional Python. Note that it helps to begin with the right data structure for a job, an optimization itself.

    # Rewriting Python algorithms to use NumPy takes some work since array objects need to be declared using NumPy’s syntax. But NumPy uses Python’s existing idioms for actual math operations (+, -, and so on), so switching to NumPy isn’t too disorienting in the long run.

    # ------------------------------------------------ 

    # Move math to Numba

        # Another powerful library for speeding up math operations is Numba. Write some Python code for numerical manipulation and wrap it with Numba’s JIT (just-in-time) compiler, and the resulting code will run at machine-native speed. Numba not only provides GPU-powered accelerations (both CUDA and ROC), but also has a special “nopython” mode that attempts to maximize performance by not relying on the Python interpreter wherever possible.

        # Numba also works hand-in-hand with NumPy, so you can get the best of both worlds—NumPy for all the operations it can solve, and Numba for all the rest.
        # Try Multiprocessing
    # Multiprocessing can bring large performance increases to a Python script, but it can be difficult to implement properly compared to other methods mentioned in this post.
    # Most modern consumer computers have 2–16 cores. Python is generally limited to a single core when processing code, but using the multiprocessing library allows us to take advantage of more than one. In very CPU-bound problems, dividing the work across several processors can really help speed things up.
    def multiprocess(cube):    
    cores = cpu_count()
    cube_parts = np.array_split(cube, cores, axis=2)
    with Pool(cores) as p:
        parts = p.map(filterfunc.filterfunc, cube_parts)
        try:
                return np.concatenate(parts, axis = 2)
        except ValueError:
            print("Array provided is smaller than # of cores available")
    filtered_pool = multiprocess(biggercube)
    # Time: 35.566 seconds

    filtered_loop = filterfunc.filterfunc(biggercube)
    # Time: 98.99 seconds

    # In this situation, I have a really large three-dimensional matrix that consists of thousands of satellite images stacked on top of one another. I need to apply a filter to every pixel through the entire time series. This can take a considerable amount of time to be repeated for every pixel of the image, so we can use multiprocessing to split the work up among all of the available processors on the machine. To do this, I simply split the cube up into as many chunks as there are available processors and apply the function to each chunk. Once all the chunks are finished, I simply concatenate them to get a final product.
    # Keep in mind that multiprocessing can’t compensate for unoptimized code. Oftentimes I leave multiprocessing as a last step after the code I am running is as fast as I can make it. We can see here that despite spreading the work across 24 cores, we only achieved a 3x speed improvement. This is due to the overhead of splitting/recombining the data and managing the multiprocessing pool.
    # Since multiprocessing pools have a decent amount of overhead, they tend to work best in situations like this where I am out of options to speed this code up more. Instead of optimizing filterfunc further, I divide the problem across more workers. Imagine Apple needed to double the phones they produce. They could spend more time training their workers to produce them more efficiently, or they could just hire a ton of people off the street. There is likely a balance of the two that will achieve optimal results.

    # ---------------------------------------
    # Use a C library
        # NumPy’s use of libraries written in C is a good strategy to emulate. If there’s an existing C library that does what you need, Python and its ecosystem provide several options to connect to the library and leverage its speed.

        # The most common way to do this is Python’s ctypes (https://docs.python.org/3/library/ctypes.html) library. Because ctypes is broadly compatible with other Python applications (and runtimes), it’s the best place to start, but it’s far from the only game in town. The CFFI(https://cffi.readthedocs.org/en/latest/) project provides a more elegant interface to C. Cython (see below) also can be used to wrap external libraries, although at the cost of having to learn Cython’s markup.

        # One caveat here: You’ll get the best results by minimizing the number of round trips you make across the border between C and Python. Each time you pass data between them, that’s a performance hit. If you have a choice between calling a C library in a tight loop versus passing an entire data structure to the C library and performing the in-loop processing there, choose the second option. You’ll be making fewer round trips between domains.

# Avoid Global Variables
    # We generally learn pretty early on in a computer science program that global variables in Python aren’t best practice. It is usually preferable to use local variables to keep better track of scope and memory usage. But beyond memory usage, Python is also slightly faster at retrieving local variables than global ones. So, it is simply best to avoid global variables when possible.

# Try Multiple Solutions

    # We saw with the Numpy examples that taking time to consider the data structures and methods you are using can have a major impact on the speed of your code. When we first start learning Python, being able to solve a problem in multiple ways is nice. But, there is often a solution that is faster than the rest and sometimes it comes down to just using a different method or data structure.
    # Take counting the occurrences of letters in a long piece of text. collections.Counter is generally a very fast way to count unique items in a data structure. However, Python has a method that is better optimized for working specifically with strings.
    from collections import Counter
    sequence = "AGAGKTAGAT" * 1000000 
    def count_string(seq):
        return [seq.count("A"), seq.count('G'), seq.count('T'), seq.count('K')]
    def count_Counter(seq):
        counter = Counter(seq)
        return [counter["A"], counter["G"], counter["T"], counter["K"]]

    count_string(sequence)
    # Time: 17.2 ms 

    count_Counter(sequence)
    # Time: 318 ms

    # Here we can see how the built-in str.count method is much faster at this specific task. This is because Counter() is a generic tool that can be used to count much more than just characters in a string, while str.count is heavily optimized to search a string for characters. That means that str.count gets to work with the underlying C char and doesn’t have to deal with iterating through Python strings.

# Memorize (cache) repeatedly used data

    # Never do work a thousand times when you can do it once and save the results. If you have a frequently called function that returns predictable results, Python provides you with options to cache the results into memory. Subsequent calls that return the same result will return almost immediately.

    # Various examples show how to do this; my favorite memoization is nearly as minimal as it gets. But Python has this functionality built in. One of Python’s native libraries, functools, has the @functools.lru_cache decorator, which caches the n most recent calls to a function. This is handy when the value you’re caching changes but is relatively static within a particular window of time. A list of most recently used items over the course of a day would be a good example.

    # Note that if you’re certain the variety of calls to the function will remain within a reasonable bound (e.g., 100 different cached results), you could use @functools.cache instead, which is more performant.

    # ----------------------------------

    # Memoization is a process where you do not repeat the same work over and over again even if it is a function whose value has already been calculated previously. Python provides you with the option of a cache that will give you the ability to instantly fetch results of functions that have been previously computed. These special functionalities of python are known as decorators and you can use them in your code to speed up your code.

    import timeit
    def fib(n):
        if n < 2:
            return n
        else:
            return fib(n-1) + fib(n-2)
    t1 = timeit.Timer("fib(40)", "from __main__ import fib")
    print(t1.timeit(1))
    # 47.392615799999994

    # Add the following two lines of code :

    from functools import lru_cache
    @lru_cache(maxsize=100)
    # 5.8000000000002494e-05

    # Shocking isn’t it? This is the power of LRU_Cache in the functools library. You can set a custom value to the LRU Cache or set it to ‘None’ to store all. This is used to store values that are frequently repeated within a stipulated frame of time. For example maybe the most recently retrieved items over the past 24 hours or a value which will be called multiple times for the next 24 hours.

    # ---------------------------------
    # Memoization is a specific type of caching that optimizes software running speeds. Basically, a cache stores the results of an operation for later use. The results could be rendered web pages or the results of complex calculations.
    # You can try this yourself with calculating the 100th Fibonacci number. If you haven’t come across these numbers, each one is the sum of the previous two numbers. Fibonacci was an Italian mathematician who discovered that these numbers cropped up in lots of places. From the number of petals on a flower to legs on insects or branches on a tree, these numbers are common in nature. The first few are 1, 1, 2, 3, 5.
    # One algorithm to calculate these is:

    def fibonacci(n):
      if n == 0: # There is no 0'th number
        return 0
      elif n == 1: # We define the first number as 1
        return 1
      return fibonacci(n - 1) + fibonacci(n-2)

    # When I used this algorithm to find the 36th Fibonacci number, fibonacci(36), my computer sounded like it was going to take off! The calculation took five seconds, and (in case you’re curious) the answer was 14,930,352.
    # When you introduce caching from the standard library, however, things change. It takes only a few lines of code.

    import functools
    @functools.lru_cache(maxsize=128)
    def fibonacci(n):
      if n == 0:
        return 0
      elif n == 1:
        return 1
      return fibonacci(n - 1) + fibonacci(n-2)

    # In Python, a decorator function takes another function and extends its functionality. We denote these functions with the @ symbol. In the example above, I’ve used the decorator functools.lru_cache function provided by the functools module. I’ve passed the maximum number of items to store in my cache at the same time as an argument. There are other forms of decorator caching, including writing your own, but this is quick and built-in. How quick? Well, this time the calculation took 0.7 seconds, and reassuringly, the answer was the same.

# Always use a C library wherever possible
    # As you have already seen the use of NumPy along with C libraries and how powerful it can be. A similar concept can be applied to other libraries and functions as well. Python libraries are not as efficient as Cones and hence if you have a choice or get an opportunity to use a C library, always go for the C library one. They are faster and more efficient than their respective Python libraries. Python’s Ctypes library is a prime example that is compatible with Python runtime and leverages the benefits of C.

    # You will be able to get the best results by reducing the number of trips from C to Python as data passing between them is a costly operation. For example consider two scenarios where you are passing one value at a time in a loop to C from Python, computing and sending it back and in another case, you pass a list to C, do your computation there and send the result back. Always go for the second option as it is much faster and efficient in this method.


# Convert to Cython
    # If you want speed, use C, not Python. But for Pythonistas, writing C code brings a host of distractions—learning C’s syntax, wrangling the C toolchain (what’s wrong with my header files now?), and so on.

    # Cython (http://cython.org/) allows Python users to conveniently access C’s speed. Existing Python code can be converted to C incrementally—first by compiling said code to C with Cython, then by adding type annotations for more speed.

    # Cython isn’t a magic wand. Code converted as-is to Cython doesn’t generally run more than 15 to 50 percent faster because most of the optimizations at that level focus on reducing the overhead of the Python interpreter. The biggest gains come when you provide type annotations for a Cython module, allowing the code in question to be converted to pure C. The resulting speedups can be orders-of-magnitude faster.

    # CPU-bound code benefits the most from Cython. If you’ve profiled (you have profiled, haven’t you?) and found that certain parts of your code use the vast majority of the CPU time, those are excellent candidates for Cython conversion. Code that is I/O bound, like long-running network operations, will see little or no benefit from Cython.

    # As with using C libraries, another important performance-enhancing tip is to keep the number of round trips to Cython to a minimum. Don’t write a loop that calls a “Cythonized” function repeatedly; implement the loop in Cython and pass the data all at once.

    # -----------------------------------

    # Cython offers C-like performance with code that is written mostly in Python. Cython makes it possible to compile parts of your Python code to C code. This way, you can convert crucial parts of an algorithm to C, which will generally offer a tremendous performance boost.

    # Cython is a superset of the Python language, meaning it adds extras to the Python syntax. It’s not a drop-in replacement like PyPY. It requires adaptions to your code and knowledge of the extras Cython adds to the language.

    # With Cython, it is also possible to take advantage of the C++ language, because part of the C++ standard library is directly importable from Cython code.

    # Cython is particularly popular among scientific users of Python. A few notable examples:

        # The SageMath computer algebra system depends on Cython, both for performance and to interface with other libraries
        # Significant parts of libraries SciPy, pandas and scikit-learn are written in Cython.
        # The XML toolkit, lxml, is written mostly in Cython


# Go parallel with multiprocessing

    # Traditional Python apps—those implemented in CPython—execute only a single thread at a time, in order to avoid the problems of state that arise when using multiple threads. This is the infamous Global Interpreter Lock (GIL). That there are good reasons for its existence doesn’t make it any less ornery.
    # The GIL has grown dramatically more efficient over time but the core issue remains. A CPython app can be multithreaded, but CPython doesn’t really allow those threads to run in parallel on multiple cores.
    # To get around that, Python provides the multiprocessing module to run multiple instances of the Python interpreter on separate cores. State can be shared by way of shared memory or server processes, and data can be passed between process instances via queues or pipes.
    # You still have to manage state manually between the processes. Plus, there’s no small amount of overhead involved in starting multiple instances of Python and passing objects among them. But for long-running processes that benefit from parallelism across cores, the multiprocessing library is useful.
    # As an aside, Python modules and packages that use C libraries (such as NumPy or Cython) are able to avoid the GIL entirely. That’s another reason they’re recommended for a speed boost.

    # ---------------------------------

    # Most software is I/O bound and not CPU bound. In case these terms are new to you:

        # I/O bound — your software is mostly waiting for input/output operations to finish. This is often the case when fetching data from the network or slow storage.
        # CPU bound — your software maxes out the CPU. It uses all CPU power to produce the needed results.

    # While waiting for answers from the network or disk, you can keep other parts running using multiple threads.
    # A thread is an independent sequence of execution. Your Python program has, by default, one main thread. But you can create more of them and let Python switch between them. This switching happens so fast that it appears like they are running side by side simultaneously.
    # Threads are independent sequences of execution, sharing the same memory space. Image © by author
    # But unlike other languages, Python threads don’t run simultaneously — they take turns instead. The reason for this is a mechanism in Python called the Global Interpreter Lock (GIL). This, together with the threading library is explained fully in my article on Python concurrency (https://towardsdatascience.com/concurrency-in-python-e770c878ab53).
    # The takeaway is that threads will make a big difference for I/O bound software, but are useless for CPU bound software.
    # Why is that? It’s simple. While one thread is waiting for a reply from the network, other threads can continue running. If you make a lot of network requests, threads can make a tremendous difference. If your threads are doing heavy calculations instead, they are just waiting for their turn to continue. Threading would only introduce more overhead.
    # The takeaway is that threads will make a big difference for I/O bound software, but are useless for CPU bound software.
    # Why is that? It’s simple. While one thread is waiting for a reply from the network, other threads can continue running. If you make a lot of network requests, threads can make a tremendous difference. If your threads are doing heavy calculations instead, they are just waiting for their turn to continue. Threading would only introduce more overhead.

# Know what your libraries are doing

    # How convenient it is to simply type include xyz and tap into the work of countless other programmers! But you need to be aware that third-party libraries can change the performance of your application, not always for the better.

    # Sometimes this manifests in obvious ways, as when a module from a particular library constitutes a bottleneck. (Again, profiling will help.) Sometimes it’s less obvious. Example: Pyglet, a handy library for creating windowed graphical applications, automatically enables a debug mode, which dramatically impacts performance until it’s explicitly disabled. You might never realize this unless you read the documentation. Read up and be informed.

# Run with PyPy

    # CPython, the most commonly used implementation of Python, prioritizes compatibility over raw speed. For programmers who want to put speed first, there’s PyPy (http://www.pypy.org/), a Python implementation outfitted with a JIT compiler to accelerate code execution.

    # Because PyPy was designed as a drop-in replacement for CPython, it’s one of the simplest ways to get a quick performance boost. Many common Python applications will run on PyPy exactly as they are. Generally, the more the app relies on “vanilla” Python, the more likely it will run on PyPy without modification.

    # However, taking best advantage of PyPy may require testing and study. You’ll find that long-running apps derive the biggest performance gains from PyPy, because the compiler analyzes the execution over time. For short scripts that run and exit, you’re probably better off using CPython, since the performance gains won’t be sufficient to overcome the overhead of the JIT.
    
    # ----------------------------

    # You are probably using the reference implementation of Python, CPython. Most people do. It’s called CPython because it’s written in C. If you are sure your code is CPU bound (see #3 if you don’t know this term) you should look into PyPy, an alternative to CPython. It’s, potentially, a quick fix that doesn’t require you to change a single line of code.

    # PyPy claims that, on average, it is 4.4 times faster than CPython. It does so by using a technique called just-in-time compilation (JIT). Java and the .NET framework are other notable examples of JIT compilation. In contrast, CPython uses interpretation to execute your code. Although this offers a lot of flexibility, it’s also very slow.

    # With JIT, your code is compiled while running the program. It combines the speed advantage of ahead-of-time compilation (used by languages like C and C++) with the flexibility of interpretation. Another advantage is that the JIT compiler can keep optimizing your code while it is running. The longer your code runs, the more optimized it will become.

    # PyPy has come a long way over the last few years, and can generally be used as a drop-in replacement for Python 2 and 3. It works flawlessly with tools like Pipenv as well. Give it a try!

    # ----------------------------------

    # AOT/JIT-compiled

    # Some Python interpreters are more optimal than others. Some use JIT compiling (like PyPy) and others compile directly to native CPU instructions (like Nuitka). Try one of these to see if they optimize your program enough to push it over the needed time limits.

# Implement caching. 
    # This can be a big optimization if you perform many repeated lookups from disk, the network, and databases.

# Reuse objects:
    # instead of creating a new one on each iteration. Python has to clean up every object you created to free memory. This is called garbage collection. The garbage collection of many unused objects can slow down your software considerably.

# Using Asyncio
    # Asyncio is a relatively new core library in Python. It solves the same problem as threading: it speeds up I/O bound software, but it does so differently.
    # I’m going to admit right away I’m not a fan of (asyncio) in Python yet. It’s fairly complex, especially for beginners. Another problem I encountered, is that the asyncio library has evolved a lot in the past years. Tutorials and example code on the web is often outdated. That doesn’t mean it's useless though. It’s a powerful paradigm that is used in many high-performance applications, like the FastAPI REST framework. The website Real Python has a nice guide (https://realpython.com/async-io-python/) on asyncio if you’re interested.



# Using more processors at once

    # If your software is CPU-bound, you can often rewrite your code so that you can use more processors at the same time. This way, you can linearly scale the execution speed.
    # This is called parallelism. Not all algorithms can be made to run in parallel. It is impossible to parallelize a recursive algorithm, for example. But there’s almost always an alternative algorithm that can work in parallel just fine.
    # There are two ways of using more processors:

        # Using multiple processors and/or cores within the same machine. In Python, we can do this with the multiprocessing library.
        # Using a network of computers to use many processors, spread over multiple machines. We call this distributed computing.

    # This article on Python concurrency focusses on ways to scale your Python software within the bounds of a single machine. It also covers the multiprocessing library. If you decide this is what you need, definitely check it out.
    # The multiprocessing library, unlike the threading library, bypasses the Python Global Interpreter Lock. It does so by actually spawning multiple instances of Python. So instead of threads taking turns within a single Python process, you now have multiple Python processes running your code at once.  
    # The multiprocessing library is very similar to the threading library. A question that might arise is: why should you even consider threading? The answer can be guessed. Threading is ‘lighter’: it requires less memory since it only requires one running Python interpreter. Spawning new processes has its overhead as well. So if your code is I/O bound, threading is likely good enough.
    # Once you implemented your software to work in parallel, it’s a small step further to use distributed computing with the likes of Hadoop. By leveraging cloud computing platforms, you can scale up with relative ease these days. You can process huge datasets in the cloud, and use the results locally, for example. With the hybrid way of operating, you can save some cash, since computing power in the cloud is pretty costly.


# Don’t construct a set for a conditional.

    # Sometimes you might find yourself wanting to optimize your code with something like this:
    if animal in set(animals):
    # This idea seems to make sense. There might be a lot of animals, and de-duplicating them feels like it might be faster.
    if animal in animals
    # Even though there may be significantly more animals in the list to check, the interpreter is optimized so much that applying the set function is likely to slow things down. Checking “in” a long list is almost always a faster operation without using the set function.


# Vectorization
    # Try to use Numpy functions(Vectorized) as much as possible and avoid loops and if conditions(can use np.where() instead). vectorizing a non vectorized functions using np.vectorize() won’t improve the speed.


# Cythonize functions
    # In case if you can’t avoid the loops, Cythonize functions. This is the best possible option in my opinion.

# Stick with the proper PEP8 guidelines.


# Use tuple instead of lists or sets if the collection doesn’t need modifications.


# Use for loop over while loop wherever possible.

# Use Numpy arrays instead of list/tuple if the elements are of same datatype.

