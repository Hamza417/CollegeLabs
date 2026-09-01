x = "awesome"

def myfunc():
    global x
    x = "fantastically global"
    print("Python is " + x)

myfunc()

print("Python is " + x)