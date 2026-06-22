# defination and property of tuple
# 1. tuple is a data structure in python used to store multiple data of diff. types with comma(,) in round bracket
# 2. immuatble
# 3. support indexing slicing and ordered

# creation of tuple
t1=(50,40,30)
print(type(t1))

t1,t2,t3=(50,40,30)
print(t1)
print(t2)
print(t3)
print(type(t1))

t1,t2,t3=(50,40,"dev")
print(t1)
print(t2)
print(t3)
print(type(t3))

# indexing and slicing
marks_tuple=(50,55,69,34,89)
print(marks_tuple[-1])
print(marks_tuple[::-1])

# mutability
marks_tuple=(50,55,69,34,89)
marks_tuple[2]=500
print(marks_tuple)

# traversing
#1. waf to extraxt all number greter then 55, 
def tuple_fun(m):
    new_value=[]
    for i in m:
        if i >=55:
            new_value.append(i)
    return new_value
marks_tuple=(50,55,69,34,89)
res=tuple_fun(marks_tuple)
print(res)

# waf to sum of indices of tuple
marks_tuple=(50,55,69,34,89)
s=0
for i in range(len(marks_tuple)):
    s+=i
print(s)

