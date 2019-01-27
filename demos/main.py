# Arithmetic operators
x = 3
y = 2
print("x + y = ",x+y)
print("x - y = ",x-y)
print("x * y = ",x*y)
print("x / y = ",x/y)
print("x ** y = ",x**y)
print("x // y = ",x//y)
print("x % y = ", x%y)

# Comparison operators

print(" x > y is :", x>y)
print(" x < y is :", x<y)
print(" x = y is :", x == y)
print(" x != y is :", x != y)
print(" x >= y is :", x >= y)
print(" x <= y is :", x <= y)

# Logical operators
m = 0
n = 1

print("m and n or m:", m and n or m)
print("m or n :", m or n)
print("not m: ", not m)


# Bitwise operators

x = 3
y = 2

print("x & y :", x&y)
print("x | y :", x|y)
print(" ~ y :", ~y)
print("x ^ y :", x^y)
print("x << y :", x<<y)
print("x >> y :", x>>y)

# Assignment operators
p = 3
q = 4
p+=q # p = p+q
print("p+=q :", p)
p = 3
p-=q # p =  p-q
print("p-=q :" ,p)
p=3
p*=q   #  p = p*q
print("p*=q :", p)
p=3
p/=q     # p = p / q
print("p/=q :", p)

#  if else demo

a = 100

if a>1000:
    print(" a is a large number")
elif a == 1000:
    print("a is 1000")
else:
    print("a is a small number")

m = 2

if m is 2:
    print(" m ==2")


# For loops demo

n = (4,5,65,676)
for i in [2,3,4,5]:
    print(i)

for j in n:
    if j>50:
        break
    print(j)

# While loop demo

t = 10

while t>0 :
    if t==3:
        t -= 1
        continue
    print(t)
    t-=1