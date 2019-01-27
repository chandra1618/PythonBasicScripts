# This program demonstrates various data types in python

# Numbers
# Lists
# Tuples
# Sets
# Dictionary
# Strings

# 1. Numbers
# Integers
# Floats
# Complex numbers

print(" ======================== Demo of numbers ========================= ")
a = 12  # Integer
b = 4.5 # Float
c = 5j+6 # Complex

j = a
m,n = 6,7.56

print(a,b,c)
print("variable a is of type : ",type(a))
print("variable b is of type : ",type(b))
print("variable c is of type : ",type(c))
print("J = ",j)
print("m , n =",m,n)

# 2. Lists
print(" ======================== Demo of list ========================= ")
L = [1,2,3,4]
print("L : ",L)
print("variable L is of type : ",type(L))
print(L[1])
L[0] = 120
print(L[2:4])
print(L[:])
L.append(4)
print(L)
print("Number 4 occurs :",L.count(4)," times ")
print("index of 4 is : ", L.index(4))
L2 = [[1,2,3],[3,5,6]]

print("L2",L2[1][2])

# 3. Tuples
print(" ======================== Demo of tuples ========================= ")
T = (31,12,12,23)
print(T)
print(T[0])
print(T.index(12))
print(T.count(12))


# 4. Sets
print(" ======================== Demo of sets ========================= ")
S = {1,2,3,4}
print(S)
S.add(5)
print(S)
S.discard(2)
print(S)
S.add(1)
print(S)


# Dictionary
print(" ======================== Demo of Dictionary ========================= ")
D = {1:'one',2:3,5.5:5.6}
print(D)
print(D.get(5.5))
print("keys: ",D.keys())
D.pop(1)
print(D)
print("values : " ,D.values())
#========= conversion ================
print(float(2))
print(int('45'))
print(str(34))
print(list({1,3,4}))