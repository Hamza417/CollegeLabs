# slicing test

n = "this is a string"

print(n[0:4])  # this
print(n[5:7])  # is
print(n[8:])   # a string

# This will print with whitespaces
print(n[0:4] + n[4:5] + n[5:7] + n[7:8] + n[8:])  # this is a string

