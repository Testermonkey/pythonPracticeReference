age = 18
if age>=18:
    print("you are now an adult")

temp = 25
if temp >= 30:
    print("its warm outside")
else:
    print("its not to hot")

res = 85
if res>= 90:
    grade="A"
elif res >= 80:
    grade = "B"
elif res >= 70:
    grade= "C"
elif grade >= 60:
    grade="D"
else:
    grade = "F"
print(f"Your grade is {grade}")

fruits = ["apple", "banana", "grape", ]
for fruit in fruits:
    print(f"Current fruit : {fruit}")

for num in range(1,6):
    print(f"num in range: {num}")

cnt =0
print(f"while")
while cnt < 5:
    print(f"Count: {cnt}")
    cnt +=1

print(f"for")
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 ==0:
        print(f"skipping this even number: {num}")
        continue
    print(f"Current number: {num}")

print(f"Range")
for i in range(3):
    for j in range(3):
        print(f"i: {i} j: {j}")

print(f"recursive")
def recursive(i,j):
    if i < 3:
        if j < 3:
            print(f"i: {i}  j: {j}")
            recursive(i, j+1)
        else:
            recursive(i+1,0)
    else:
        return
    
recursive(0,0)