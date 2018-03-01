def simple_gen():
    for i in [1,2,3]:
        yield i

# Get generator from function
gen = simple_gen()

print("Type: ", type(gen))

# Iteration through  generator
print("Iter #1: ", next(gen))
print("Iter #2: ", next(gen))
print("Iter #3: ", next(gen))

# Generator is empty, StopIteration
next(gen)