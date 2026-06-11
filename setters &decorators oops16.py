 # Setters and Decorators in Python:-----------------------------------

class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@anshdhairya99@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname ==None:
            return "Email is not set. Please set it using of setter"
        return f"{self.fname}.{self.lname}@anshdhairya99@gmail.com"
    
    @email.setter
    def email(self, string):
        print("Setting Now")
        names = string.split("@") [0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

        @email.deleter
        def email(self):
            self.fname = None
            self.lname = None





hindustani_supporter = Employee("Hindustani","Supporter")
#nikhil_raj_pandey = Employee("Nikhil","Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@anshdhairya99@gmail.com"
print(hindustani_supporter.fname)

del (hindustani_supporter.email)
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.perry@codewithharry.com"

print(hindustani_supporter.email)

