from sympy import E


class students:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sort_age(self, other):
        age_students = []
        age_students.append(self.age)
        age_students.append(other.age)
        x = age_students.sort()
        return x
    
    def age_square(self):
        x = self.age
        return x


student_1 = students("Ben" , "24")
student_2 = students("Anabel" , "20")

print(students.sort_age(student_1 , student_2))

tuple_list = [(1 , 2) , (3 , 5) , (8 , 5)]
first_tuple = []
a = tuple_list[0][1]

for i in range(len(tuple_list)):
    first_tuple.append(tuple_list[i][0])


print(first_tuple)
print(students.age_square(student_1))

b = [1 , 10 , 19 , 28 , 37]

counter = 0
for i in range( len(b) - 1 ):
    if b[i] > 15:
        b.pop(i)
    else:
        pass
          
print(b)

