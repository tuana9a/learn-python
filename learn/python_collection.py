thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])
print(thistuple[2])

#create tuple with one value
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

seq = range(11)
print(seq)
seq2 = [x * 2 for x in seq]
print(seq2)
seq3 = [x for x in seq if x % 3 == 0]
print(seq3)
seq4 = [(x, x**2) for x in seq if x % 3 == 0]
print(seq4)
seq5 = [x for x in "tuana9a" if x not in 'ta']
print(seq5)