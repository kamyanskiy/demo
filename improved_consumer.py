from functools import wraps

def coro(f):
    def wrapper(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrapper

@coro
def simple_consumer():
    results = []
    while True:
        x, y = (yield)
        if x == 'r':
            print("Collected results: ", results)
            continue
        res = x + y
        results.append(res)
        print("Sum", res)


# Call function returns initiated generator object
gen = simple_consumer()

print(type(gen))

# Check: we don't need to start generator with send None
"""
gen.send(None)

Traceback (most recent call last):
  File "/home/biceps/work/demo/improved_consumer.py", line 30, in <module>
    gen.send(None)
  File "/home/biceps/work/demo/improved_consumer.py", line 14, in simple_consumer
    x, y = (yield)
TypeError: 'NoneType' object is not iterable

"""

# Use generator
gen.send((1,1))
gen.send((2,2))

# Show collected results
gen.send(('r', None))

# Close generator
gen.close()

# We can't use closed generator
"""
gen.send((3,3))

Traceback (most recent call last):
  File "/home/biceps/work/demo/simple_consumer.py", line 36, in <module>
    gen.send((3,3))
StopIteration
"""