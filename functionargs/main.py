# Required arguments =====================================

def function1(str):
    print(str)
    return

function1("Hello world")

# Keyword arguments=======================================
def function2(str1,str2):
    print(str1)
    print(str2)
    return

function2(str2 = "my string",str1 = "hi there")

def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )

# Default arguments ======================================

def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# Variable length arguments

def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )