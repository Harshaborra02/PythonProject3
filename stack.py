# s="Hello"
# s1=[]
# for i in range(len(s)):
#     s1.append(s[i])
# for i in range(len(s1)):
#     print(s1.pop(),end="")

# s="{[())]}"
# s1=[]
# b=False
# for i in range(len(s)):
#     if s[i]=="(" or s[i]=="{" or s[i]=="[":
#         s1.append(s[i])
#     elif len(s1)!=0 and ((s1[-1]=="(" and s[i]==")") or (s1[-1]=="{" and s[i]=="}") or (s1[-1]=="[" and s[i]=="]")):
#         s1.pop()
#     else:
#         b=True
#         break
# if len(s1)==0 and b==False:
#     print("Valid")
# else:
#     print("Invalid")


# l=[10,20,30,40,50,60,70]
# l1=[]
#
# c=len(l)//2
# for i in range(c):
#     l1.append(l.pop())
# l.pop()
# for i in range(len(l1)):
#     l.append(l1.pop())
# print(l)

s=[10,20,30,40,50,60]
temp=[]
c=len(s)//2
temp=[]
for i in range(c):
    temp.append(s.pop())
s.pop()
for i in range(len(temp)):
    s.append(temp.pop())
if len(s)%2!=0:
    c=len(s)//2
    for i in range(c):
        temp.append(s.pop())
    s.pop()
    for i in range(len(temp)):
        s.append(temp.pop())
print(s)

s="madam"
stack=[]
temp=""
for i in s:
    stack.append(i)
    # print(stack)
for i in range(len(stack)):
    temp=temp+stack.pop()
if temp==s:
    print("Palindrome")
else:
    print("Not a Palindrome")
# print(stack,temp)
s="23*54*+"
stack=[]
sum=0
for i in s:
    if i.isdigit():
        stack.append(int(i))
    elif i=="*":
        for i in stack:
            sum=sum*stack.pop()
    elif i=="+":
        for i in stack:
            sum=sum+stack.pop()
print(sum)

s=list(map(str,input().split(" ")))
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
d=dict()
for i in s1:
    c=s.count(i)
    print(c)
    d.update({i:c})
print(d)

