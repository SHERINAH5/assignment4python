student_names = ['Sandra','Patricia','Phionah','Anitah',]
student_marks = [80, 56, 78, 90]
data = ['Sandra', 90, 'Kamokya']

print(student_names, type(student_names))
student_names.append('Ruth')
print(student_names)
student_names.insert(2,'Suzan')
print(student_names)
#ASSIGNMENT
#slicing print; Patricia, Faith, Anitah
print(student_names[1:4])
#Add Masha at the forth position
student_names.insert(3,'Masha')
print(student_names)
#update the name phionah to Aladinah
student_names[4] = 'Aladinah'
print(student_names)
#display all the length of the student list
print(len(student_names))

#print all the student names using a for loop
for name in student_names:
    print(name)
#calculate the total marks for the students  ans = 304
total_marks = sum(student_marks)
print(total_marks)






