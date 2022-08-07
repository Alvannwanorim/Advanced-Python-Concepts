class Person:
    def name(self):
        print("hellow world", self)

    def age(self, age):
        self.age =age
        print("age ",age, "new here")
p1 = Person()
p2 = Person()
p1.age(23)