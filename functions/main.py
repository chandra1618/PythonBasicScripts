# Functions in python

def addition(a,b):
    "This example demonstrares how to define functions"
    return a+b

def comparison(m,n):
    if m<n:
        return "m is smaller than n"
    elif m == n:
        return "m is equal to n"
    else:
        return "m is greater than n"

res1 = addition(3,4)
res2 = comparison(6,0.1)

print(res1)
print(res2)