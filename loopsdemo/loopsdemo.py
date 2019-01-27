# For loop demo
#======================================
for i in range(1,10) :
    if (i%2) ==0:
        print("i = ",i)
    else:
        pass
#======================================
for j in [1,2,3,4,5]:

    if j > 3:
        break
    print("j = ", j)
#=======================================
for k in "hello":
    print(k)
#=======================================
mat = [100,200,300,400,500]

for l,m in enumerate(mat):
    print(l,m)
#=======================================
# While loop demo
lk = 5
p=0
while p <lk:
    p+=1;
    print(p)