# from functools import reduce
# num=list(map(int,input().split()))
# res=reduce(lambda x,y:x if x>y else y,num)
# print(res)

# sales=[{"item":"Pen","price":10,"qty":5},
#        {"item":"Bag","price":500,"qty":0},
#        {"item":"Book","price":120,"qty":3},
#        {"item":"Eraser","price":5,"qty":10}]
# new_list=[]
# for i in sales:
#     for value in i.values():
#         res=list(filter(lambda x:x,i.values()))
#         if res not in new_list:
#             new_list.append(res)
# # print(new_list)
# is_sum=0
# for i in new_list:
#     if len(i)>2:
#         is_sum+=i[1]*i[2]
# print(is_sum)
# students=[{"name":"ravi","score":45},
#           {"name":"sneha","score":78},
#           {"name":"kiran","score":60},
#           {"name":"divya","score":92}]
# new_list=[]
# for i in students:
#     for value in i.values():
#         res=list(filter(lambda x:x,i.values()))
#         if res[1]>=60:
#             if res not in new_list:
#                 new_list.append(res)
# print(dict(new_list))
from functools import reduce
sales=[{"item":"Pen","price":10,"qty":5},
       {"item":"Bag","price":500,"qty":0},
       {"item":"Book","price":120,"qty":3},
       {"item":"Eraser","price":5,"qty":10}]
res=list(filter(lambda x: x["qty"]>0,sales))
res=list(map(lambda x:x["price"]*x["qty"],res))
res=reduce(lambda x,y:x+y,res)
print(res)
print(res)
students = [
    {"name": "Ravi", "score": 45},
    {"name": "Sneha", "score": 78},
    {"name": "Kiran", "score": 60},
    {"name": "Divya", "score": 92}]
result = list(filter(lambda x: x["score"] >= 60, students))
result = list(map(lambda x: {**x, "Grade": "Pass"}, result))
result = sorted(result, key=lambda x: x["score"], reverse=True)
new_list=[]
for i in result:
    new_list.append(i)
print(new_list)