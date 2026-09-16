t = (1, 2, 3, 4, 4)

for i in range(len(t)):
    print("index:", i, "value:", t[i])

print()

# print in reverse
for i in range(len(t) - 1, -1, -1):
    print("index:", i, "value:", t[i])

print()

# tuple methods
print(t.count(4)) # count the number of occurrences of 4 in the tuple
print(t.index(2)) # find the index of the first occurrence of 2 in the tuple