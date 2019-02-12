#44.1.2 Override Explicitly

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

class Teacher(Child):

    def override(self):
        print("TEACHER override()")


dad = Parent()
son = Child()
school = Teacher()

dad.override()
son.override()
school.override()
