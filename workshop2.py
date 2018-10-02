A = []
a = []
B = []
b = []

print("enter size for matrix 1")
size1c = int(input())
size1r = int(input())
print("enter size for matrix 2")
size2c = int(input())
size2r = int(input())

if size1c != size2r:
    print("")

try:
    while len(a) != size1c:
        for i in range(size1r):
            a = [int(x) for x in input().split()]
            if len(a) != size1c:
                print("")
            A.append(a)
except IndexError:
    pass

#The same for B with b and sizes 2

result = [[0 for x in range(size1c)] for i in range(size1r)]

for i in range(size1r):
    for j in range(size2c):
        for k in range(size2r):
            try:
                result[i][j] += A[i][k] * B[k][j]
            except IndexError:
                pass
'''
a bit about git

git init
git add filename
git commit -m
git remote add origin ...
git remote -v
git push origin master
'''

















