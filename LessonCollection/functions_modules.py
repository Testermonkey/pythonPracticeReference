def hello(name):
    print(f"hi, {name}")

hello("Ed")

def add(a,b):
    return a+b

res = add(1,2)
print(f"Sum: {res}")

def power(base, exp=2):
    return base ** exp

print(f"2^3 ", power(2,3))
print(f"2^3 ", power(2))

def concatenate(*args):
    r=""
    for arg in args:
        r += arg
    return r

print(concatenate("Hi ", "World"))
print(concatenate("Python", " ", "is", "amazing"))