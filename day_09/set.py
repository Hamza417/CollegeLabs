s = {1, 2, 3, 4, 4}

print(s)  # sets automatically remove duplicate elements

s.add(5)  # add an element to the set
print(s)
s.update([6, 7, 8])  # add multiple elements to the set
print(s)
s.remove(8)  # remove an element from the set
print(s)
s.discard(10)  # remove an element from the set, but do not raise an error if it does not exist
print(s)
