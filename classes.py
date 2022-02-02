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