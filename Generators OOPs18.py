# Generators OOPS 18.py :---------------------------------

#Iterable - __iter__ or __getitem__()
#Iterator - __next__()
#Iteration -

#for i in range(90):
#    print(i)

#def gen(n):
#    for i in range(n):
#        yield i

#g = gen(354545454545454545454545)
#print(g)

#h = "Harry"
#for c in h:
#    print(c)

h = "HARRY"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
for c in h:
    print(c)