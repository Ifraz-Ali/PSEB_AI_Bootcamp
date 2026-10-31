# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print("Hi,  i am ", self.name, "and I am ", self.age, "years old")

# s = Student("Ifraz", 20)
# s.greet()


from operator import attrgetter

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("Ifraz", 49)
s2 = Student("Babar", 65)
s3 = Student("Ahtisham", 75)

students = [s1, s2, s3]

for student in students:
    if student.score > 50:
        print(student.name, "has scored", student.score)

def top_scorer(studs):
    top_student = studs[0]
    # top = max(studs, key=lambda x: x.score)
    # top = max(studs, key=attrgetter('score'))
    # print("top", top.score)
    for stud in studs:
        if stud.score > top_student.score:
            top_student = stud
    return top_student

print("Top scorer is", top_scorer(students).name, "with score", top_scorer(students).score)
