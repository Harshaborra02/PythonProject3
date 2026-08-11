l=["song1","song2","song3","song4","song5"]
it=iter(l)
it1=iter(l)
print(next(it))
print(next(it1))
print(next(it))
print(next(it))
print(next(it1))
print(next(it))
print(it1.__next__())

class Playlist:
    def __init__(self,lst):
        self.index=0
        self.lst=lst
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.lst):
            song=self.lst[self.index]
            self.index+=1
            return song
        # else:
        #     raise StopIteration
p1=Playlist(["Irumudi","Hukum","Orrum Blood","Ayya Shear"])
p=iter(p1)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
for i in p1:
    if i is None:
        break
    print(i)


class Attendance:
    def __init__(self,students):
        self.roll_no=0
        self.students=students
    def __iter__(self):
        return self
    def __next__(self):
        if self.roll_no<len(self.students):
            name=self.students[self.roll_no]
            self.roll_no+=1
            return name
        else:
            raise StopIteration
a1=Attendance(["Harsha","Venkat","Abhi","Bunny","Madhu","Naveen"])
a=iter(a1)
print(next(a))
for i in a1:
    print(f"{i} : Present")


class Even:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            n=self.l[self.index]
            self.index+=1
            if n%2==0:
                return n
        else:
            raise StopIteration
e=Even([1,2,3,4,5,6,7,8,9])
for i in e:
    print(i)

class A:
    def __init__(self,s):
        self.s=s
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.s):
            ch=self.s[self.index]
            self.index+=1
            if ch not in "aeiou":
                return ch
        else:
            raise StopIteration
a=A("i am Harsha From Hyderabad")
for i in a:
    print(i)

class B:
    def __init__(self,s):
        self.i=0
        self.s=s
        self.is_sum=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i< len(self.s):
            self.is_sum+=ord(self.s[self.i])
            self.i+=1
            if self.i==len(self.s):
                return self.is_sum
        else:
            raise StopIteration
word=B("Harsha")
for i in word:
    print(i)


