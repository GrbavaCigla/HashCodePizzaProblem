import timeit

with open("./main.py", "r") as f:
    doc = f.read()


print("{:.10f} seconds".format(float(timeit.Timer(doc).timeit(number=1))))
print("{:.10f} average seconds".format(
    float(timeit.Timer(doc).timeit(number=10)/10)))
