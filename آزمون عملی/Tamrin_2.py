class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("=-" * 12)
        print(f"Name: {self.name} \nAge: {self.age}")
        print("=-" * 12)

    def __str__(self):
        return f"Error : lotfan yek method ra estefade konid!"


if __name__ == "__main__":
    name = input("Name : ")
    age = input("Age : ")
    try:
        age = int(age)
        s1 = Student(name, age)
        s1.greet()
    except ValueError:
        print("Error : Lotfan adad sahih vared konid.")
