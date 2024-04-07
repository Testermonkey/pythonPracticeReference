

# Given this list of students..

import random as rn
students = ["Amy", "Ben", "Cal", "Dan", "Eli", "Fay", "Guo", "Hal", "Ida", "Jed", "Ken", "Les", "Moe"]

tested_students = []
for student in students:
    student = [student, rn.randint(200, 800), rn.randint(200, 800) ]
    tested_students.append(student)

for student in tested_students:
    print(f"{student[0]}: Math:{student[1]} Verbal:{student[2]}")

# A. Loop the list of students:
# for
  # B. Generate a pair of random ints in the 200-800 range. Ints must end in 0:


# C. Print the result for the current student (stu):
print("SAT scores:\nMath: Verbal: \n")

