# def dec(func):
#     def inner(n):
#         print("Starting this Function")
#         print(func.__name__)
#         func(n)
#         print("Ending this Function")
#     return inner
# @dec
# def greet(name):
#     print(f"Hello {name}")
# print(greet.__name__)
# greet("Nikhil")

# def valid(func):
#     def inner(x,y):
#         if isinstance(x,int) and isinstance(y,int):
#             print(f"Multiplying {x} and {y}:",end=" ")
#             func(x,y)
#         else:
#             print("Arguments must be integers")
#     return inner
# @valid
# def multiply(x,y):
#     print(x*y)
#
# multiply(5,4)
#
# def login(func):
#     def inner():
#         u="Harsha"
#         p="Harsha@123"
#         if u=="Harsha" and p=="Harsha@123":
#             return func()
#         return "Invalid Credentials"
#     return inner
# @login
# def securefile():
#     return "secret file"
# print(securefile())

#manual decoration
# def my_decorator(func):
#     def wrapper():
#         print("--Before the function runs")
#         func()
#         print("--After the function runs")
#     return wrapper
# def say_hello():
#     print("Hello World!")
# say_hello=my_decorator(say_hello)
# say_hello()

# UNIVERSAL WRAPPER TEMPLATE
# def my_decorator(func):
#     def wrapper(a,b):
#         print("Before")
#         func(a,b)
#         print("After")
#     return wrapper
# def add(a,b):
#     print(a+b)
# add=my_decorator(add)
# add(3,4)

# @ SYNTAX tho
# def my_decorator(func):
#     def wrapper(name):
#         result=func(name.upper())
#         return result
#     return wrapper
# @my_decorator
# def greet(name):
#     return f"Hello,{name}"
# print(greet("Harsha"))

# Decorators with *args and **kwargs
# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         print("Before Function")
#         result=func(*args,**kwargs)
#         print("After Function")
#         return result
#     return wrapper
# @my_decorator
# def add(a,b):
#     print(a+b)
# add(3,4)

#checking
# def my_decorator(func):
#     def wrapper(a,b):
#         if isinstance(a,int) and isinstance(b,int):
#             return func(a,b)
#         return "Given Input is not an int data type"
#     return wrapper
# @my_decorator
# def add(a,b):
#     return a*b
# print(add(3,5))

#registration validation
# def valid(func):
#     usd=["Abhi","Venkat","Bunty","Vivek","Kethan"]
#     spec=["!","@","#","$","%","^","&","*"]
#     def inner(us,psd,age):
#         if us not in usd:
#             usd.append(us)
#             if len(psd)>=8:
#                 k=list(filter(lambda x:x in spec,psd))
#                 n=list(filter(lambda x:x.isdigit(),psd))
#                 u=list(filter(lambda x:x.isupper(),psd))
#                 if k and n and u:
#                     if age >=18:
#                         return func(us,psd,age)
#                     else:
#                         return "Age must be greater 17"
#                 else:
#                     return "Invalid Password"
#             else:
#                 return "Minimum length of password is 8 characters"
#         else:
#             return f"Username already Exists"
#     return inner
# @valid
# def register(username,password,age):
#     return f"{username}'s Registration Successful "
# print(register("Harsha","Harsha@123",19))
# print(register("Harsa","Asdjfjj@12",2))

# import functools
# def ann(func):
#     @functools.wraps(func)
#     def inner(x,y):
#         # print(func.__name__)
#         # print(func.__annotations__)
#         # print(func.__doc__)
#         print(x,y)
#         return func(x,y)
#     return inner
#
# @ann
# def fun(a:int,b:int)->int:
#     """Just adding a Doc for the function"""
#     return a+b
# print(fun.__name__)
# print(fun.__annotations__)
# print(fun.__doc__)
# print(fun(3,4))
# import functools
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(name):
#         return func(name)
#     return wrapper
# @my_decorator
# def greet(name:str)->str:
#     """just a greet function"""
#     return f"Hello, {name}"
# print(greet.__name__)
# print(greet.__annotations__)
# print(greet.__doc__)
# print(greet("Harsha"))

# def my_decorator(func):
#     def wrapper():
#         print("Function is Starting")
#         result= func()
#         print("Function is Done")
#         return result
#     return wrapper
# @my_decorator
# def greet():
#     print("Hello")
# greet()

#Q4.  What does @functools.wraps(func) do? Write an example showing what happens to
# __name__ with and without it.
# import functools
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
#     return wrapper
# @my_decorator
# def add(a:int,b:int)->int:
#     """using functools"""
#     return a+b
# print(add(3,4))
# print(add.__name__)
# print(add.__annotations__)
# print(add.__doc__)

# Q1.  Write a decorator called validate_positive that checks all positional arguments
# passed to a function. If any argument is negative, print an error message and
# return None without calling the function test it on a function multiply(a,b)
def my_decorator(func):
    def wrapper(a,b):



def multiple(a,b):
    return a*b
print(multiple(2,3))

