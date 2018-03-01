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

# Call function returns generator object
gen = simple_consumer()

print(type(gen))

# If generator was not initiated error occurs:
"""
gen.send((1,1))

Traceback (most recent call last):
  File "/home/biceps/work/demo/simple_consumer.py", line 15, in <module>
    gen.send((1,1))
TypeError: can't send non-None value to a just-started generator
"""

# Start generator with send None
gen.send(None)

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