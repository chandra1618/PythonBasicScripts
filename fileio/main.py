# Open a file
fo = open("E:\\python\\Scripts\\fileio\\foo.txt", "r")
out = fo.read()
fo.close()
fo = open("E:\\python\\Scripts\\fileio\\foo.txt", "w")

out = out + "\n1234567890"

fo.write(out)
fo.close()

"""
# Bitwise not operator in python
x = 10   # 0000 1010
x = ~x   # 0000 1011

print(bin(x))
print(x)

"""