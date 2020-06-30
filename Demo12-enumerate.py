
list1 = ["a","b","c","d","e"]

t = tuple()

l = list()

for i in enumerate(list1):
    print(i)
    t = t + i
    l.append(i)
    print(type(i))

print(t)

print(l)

d1 = dict(l)
print(d1)
