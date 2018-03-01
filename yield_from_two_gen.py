# Python 3.3+ - yield from

gen1 = (print(x) for x in range(0,5))
gen2 = (print(x) for x in range(5,10))

"""
def gen3():
    for i in gen1:
        yield i
    for j in gen1:
        yield j

"""

def gen3():
    print("First generator starts")
    yield from gen1
    print("Second generator starts")
    yield from gen2

# init generator
gen = gen3()
print("Show type gen:", type(gen))

# First's generator iteration
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)

# Second's generator iteration
next(gen)
next(gen)
next(gen)
next(gen)
next(gen)

"""
next(gen)

Traceback (most recent call last):
  File "/home/biceps/work/demo/yield_from_two_gen.py", line 30, in <module>
    next(gen)
StopIteration
"""
