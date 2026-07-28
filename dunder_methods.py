class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,o2):
        return self.marks>o2.marks
    def __ge__(self,o2):
        return self.marks>=o2.marks
    def __eq__(self,o2):
        return self.marks==o2.marks
    def __ne__(self,o2):
        return self.marks!=o2.marks
    def __hash__(self):
        return hash(self.marks)
    def __str__(self):
        return 1
s1=Student("Harsha",88)
s2=Student("VEnkat",88)
print(s1>s2)
print(s1>=s2)
print(s1==s2)
print(s1!=s2)
print(s1,s2)
