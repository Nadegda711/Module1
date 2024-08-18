grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a =(sum(grades[0]))/5
b =(sum(grades[1]))/4
j =(sum(grades[2]))/4
k =(sum(grades[3]))/3
s =(sum(grades[4]))/5
grades1 =(a, b, j, k, s)

students1 = list(students)
print(type(students1))
print(students1)
students1[0]=('Aaron')
students1[1]=('Bilbo')
students1[2]=('Johnny')
students1[3]=('Khendrik')
students1[4]=('Steve')
print(students1)
print(dict(zip(students1, grades1)))

