"""from sympy import E


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
        print((self.age)**2)


student_1 = students("Ben" , "24")
student_2 = students("Anabel" , "20")

print(students.sort_age(student_1 , student_2))

tuple_list = [(1 , 2) , (3 , 5) , (8 , 5)]
first_tuple = []
a = tuple_list[0][1]

for i in range(len(tuple_list)):
    first_tuple.append(tuple_list[i][0])


print(a)
print(first_tuple)
print(students.age_square(student_1))

b = [1 , 10 , 19 , 28 , 37]

counter = 0
for i in range( len(b) - 1 ):
    if b[i] > 15:
        b.pop(i)
    else:
        pass
          
d = [4 , 8 , 12 , 16 , 20]
sum = 0
for i in range(len(d)):
    sum = sum + d[i]
print(sum)




list1 = [1, 2, 5, 9, 1000]
list2 = ["q", "w", "e", "f", "g"]

for i in range(len(list1)):
    a = list2[i]
    print(a)
    list2.remove(a)



lists = (5, 10 , 15 , 20 , 25)
print(lists[1]- lists[0])"""




