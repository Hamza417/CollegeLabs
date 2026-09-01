# concatenate string with an integer

a = "this is a string"
x = 5

print(a + " " + str(x))  # this is a string5

print(a + " " + str(x) + " " + str(x * 2))  # this is a string 5 10

print(f"{a} {x} {x * 2}")  # this is a string 5 10