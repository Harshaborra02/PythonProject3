#Q1. Create a class Student with instance attributes name and marks.
# Add an instance method is_passed() that returns True if marks > 40.
# Then create 2 student objects and print whether each has passed or failed.
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         if self.marks>40:
#             return True
#         return False
# s=Student("Harsha",80)
# print(s.is_passed())
# s1=Student("Venkat",35)
# print(s1.is_passed())
#Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
# Demonstrate how this change affects all instances.
# class Employee:
#     def __init__(self,name,company_name):
#         self.name=name
#         self.company_name=company_name
#     @classmethod
#     def change_company(cls,new_name):
#         cls.new_name=new_name
#         print(cls.new_name)
# e=Employee("Harsha","TechCorp")
# e.change_company("CVCORP")
#Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.
# class MathOps:
#     def __init__(self):
#         pass
#     @staticmethod
#     def is_even(num):
#         if num%2==0:
#             return "Even"
#         return "Odd"
# m1=MathOps()
# print(m1.is_even(20))
# m2=MathOps()
# print(m2.is_even(21))
#Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.
# class Car:
#     wheels=4
#     def __init__(self,mileage):
#         self.mileage=mileage
#     def display_specs(self):
#         print(self.mileage,self.wheels)
#     @classmethod
#     def change_wheels(cls):
#         cls.wheels=5
#         # print(cls.wheels)
#     def display_specs_1(self):
#         print(self.mileage,self.wheels)
# c=Car(20)
# c.display_specs()
# c.change_wheels()
# c.display_specs_1()
#Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.
# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     @staticmethod
#     def to_fahrenheit(celsius):
#         f=celsius*5/9
#         print(f)
#     def show_conversion(self):
#         print(self.celsius)
# t=Temperature(32)
# t.to_fahrenheit(32)
# t.show_conversion()

#Q6. Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if cls.is_valid_title(t):
            return Book(t,a)
        return "Not Valid"
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
b=Book("Th","Harsha")
b1=Book.from_string("secrets to success-Venkat")
print(b1.title)
print(Book.total_books)
b2=Book.from_string("ab-Abhi")
print(b2.title)
print(Book.total_books)
#Q7. Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0
# Create two employees, show final salaries, update bonus rate, and show again.
class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def final_salary(self):
        self.base_salary=self.base_salary+(self.base_salary*Employee.bonus_rate)
        print(self.base_salary)
    @classmethod
    def update_bonus(cls,new_rate):
        cls.bonus_rate=new_rate
    @staticmethod
    def is_valid_salary(sal):
        if sal>0:
            return "Valid"
        return "Not Valid"
e=Employee("Harsha",30000)
e.final_salary()
e.update_bonus(0.3)
e.final_salary()
# print(e.is_valid_salary(30000))
e1=Employee("Venkat",25000)
e1.final_salary()
e1.update_bonus(0.1)
e1.final_salary()
#Q8. Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.
class Course:
    total_students=0
    def __init__(self,student_name):
        self.student_name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        if age>=18:
            return True
        return False
c=Course("Harsha")
c.enroll()
c.show_total()
print(c.is_eligible(18))
c1=Course("Venkat")
c1.enroll()
c1.show_total()
print(c1.is_eligible(22))

#Q9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.
class BankAccount:
    bank_name="SBI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        return False
b=BankAccount("Harsha",200)
print(b.balance,b.bank_name)
b.deposit(100)
b.change_bank_name("HDFC")
print(b.balance,b.bank_name)
b1=BankAccount("Venkat",300)
print(b1.balance,b1.bank_name)
b1.deposit(100)
b1.change_bank_name("SBI")
print(b1.balance,b1.bank_name)
#Q10. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result
class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>self.passing_marks:
            print("Passed")
        else:
            print("Failed")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if 90<=marks<100:
            return "A"
        elif 80<=marks<90:
            return "B"
        else:
            return "C"
s=Student("Harsha",50)
s.result()
s.update_passing_marks(60)
s.result()
print(s.grade_category(50))


# python methods 2
#Q1. Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
class Student:
    total_students=0
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>self.passing_marks:
            return "Passed"
        return "Failed"
    def curve_marks(self):
        self.marks=self.marks+10
    @staticmethod
    def grade(marks):
        if 90<=marks<100:
            return "A"
        elif 80<=marks<90:
            return "B"
        elif 70<=marks<80:
            return "C"
        else:
            return "D"
s=Student("Harsha",80)
print(s.is_passed())
s.curve_marks()
print(s.marks)
print(s.grade(s.marks))

#Q2. Design a class Product that:
# •	Maintains a base tax rate applicable to all products.
# •	Each product has a name and base price.
# •	Has a method to compute final price including tax.
# •	Can change tax rate for all products using one method.
# •	Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.	Creating multiple products.
# 2.	Changing the tax rate.
# 3.	Showing updated prices and validity checks.
class Product:
    base_tax=0.3
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        self.base_price+=self.base_price*self.base_tax
        print(self.base_price)
    @classmethod
    def change_tax(cls,new_tax):
        cls.base_tax=new_tax
    @staticmethod
    def is_valid(price):
        if price>0:
            return "Valid"
        return "Not Valid"
p=Product("Milk",30)
p.final_price()
p.change_tax(0.5)
p.final_price()
print(p.is_valid(p.base_price))
p1=Product("Bread",30)
p1.final_price()
print(Product.base_tax)

#Q3. Create an Employee class that:
# •	Keeps a minimum experience required for promotion (shared across all employees).
# •	Stores employee name, experience, and department.
# •	Has a method to check eligibility for promotion.
# •	Provides a function to update promotion criteria globally.
# •	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.	Creating employees from different departments.
# 2.	Changing promotion criteria.
# 3.	Displaying eligibility results and department validation.
class Employee:
    min_exp=2
    def __init__(self,name,experience,department):
        self.name=name
        self.experience=experience
        self.department=department
    def is_valid(self):
        if self.experience>=self.min_exp:
            return "Valid"
        return "Not Valid"
    @classmethod
    def change_promotion(cls,new_value):
        cls.min_exp=new_value
    @staticmethod
    def is_present(d):
        if d in ["HR","IT","Admin"]:
            return "Valid"
        return "Not Valid"
e=Employee("Harsha",3,"IT")
e1=Employee("Ram",1,"Admin")
e2=Employee("Pooja",5,"HR")
Employee.change_promotion(3)
print(e.is_valid())
print(e.is_present(e.department))

#Q4. Build a Loan class that:
# •	Has a common interest rate for all loans.
# •	Each object stores borrower name and principal.
# •	Calculates total payable amount.
# •	Provides a function to update the interest rate.
# •	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.	Creating multiple loan accounts.
# 2.	Updating interest rates.
# 3.	Checking eligibility and total repayment for borrowers.
class Loan:
    interest_rate=0.2
    def __init__(self,name,principal):
        self.name=name
        self.principal=principal
    def total_pay(self):
        self.principal+=self.principal*self.interest_rate
        print(self.principal)
    @classmethod
    def change_interest(cls,new_value):
        cls.interest_rate=new_value
    @staticmethod
    def is_valid(salary):
        return salary>20000
l=Loan("Harsha",25000)
l.total_pay()
l.change_interest(0.21)
l.total_pay()
print(l.is_valid(l.principal))

#Q5. Create a class Course that:
# •	Tracks total courses created.
# •	Each course has a title, duration, and enrolled_students.
# •	Provides a method to enroll a new student.
# •	Allows updating the minimum duration for a valid course across all instances.
# •	Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.	Creating multiple courses.
# 2.	Enrolling students.
# 3.	Updating minimum duration and checking durations.
class Course:
    total_courses=0
    def __init__(self,title,duration,enrolled_students):
        self.title=title
        self.duration=duration
        self.enrolled_students=enrolled_students
    