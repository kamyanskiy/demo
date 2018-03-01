def gen():
    for x in range(5):
        yield x

print("gen: ", type(gen()))

# Comprehension expression
f = (x for x in range(5))
print("f: ", type(f))



