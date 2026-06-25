#--------------dictionary----------
#  definition and property of dict.
# creation of dictionary
# Traversing
# In-build method
# dictionay comprehension
# assignment and class


# -------------definition and property of dictionary------------
# dict. is a data structure in python used to store multiple data in key: value formet
# orderd, mutable
# indexing by key not position
# key must be anty type of data 
# value can be any type of data
# used in fast loop

#-------------creation of dictionary------
stu_profile={'aman':'noida','rohan':'delhi'}
print(type(stu_profile))
print(stu_profile)

# in-build method
stu_marks={'aman':300,'shivam':80,'rohan':40,'abhi':45}
v=stu_marks.values()
k=stu_marks.keys()
i=stu_marks.items()
res=stu_marks.get('dev','not found')
print(v)
print(k)
print(i)
print(res)