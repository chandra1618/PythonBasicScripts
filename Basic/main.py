
# this is the first comment


#! python

# integer variables
SPAM = 1


#! python

print ("Hello, Python")


#! python
# string variable

STRING = "# This is not a comment."

print(STRING)



#! python

# integer arith

a=4
print (a)

b=12+5
print (b)

c=b%a
print (c)


#! python

# trailing comma

i = 256*256
print ('The value of i is', i)


#! python

# input and operator if

x = int(input("Please enter an integer: "))

if x < 0:
      x = 0
      print ('Negative changed to zero')
elif x == 0:
      print ('Zero')
elif x == 1:
      print ('Single')
else:
      print ('More')


#! python

# operator for:

# Measure some strings:
a = ['cat', 'window', 'defenestrate']
for x in a:
    print (x, len(x))



#! python

# range function

print (range(10))

print (range(5, 10))

print (range(0, 10, 3))


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i, a[i])



#! python

# break operator
# prime numbers

for n in range(2, 1000):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print (n, 'is a prime number')