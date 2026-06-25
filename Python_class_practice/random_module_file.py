import random
# emp_name=["aman", "kamal","deepak","shivam"]
# weight=[2,4,8,12]
# res=random.choices(emp_name,weights=weight,k=4)
# print(res)

# res=random.random()*1000
# print(int(res))

# rand_int=random.randint(1,10)
# rand_range=random.randrange(1,10)
# print(rand_int)
# print(rand_range)


# user max attempt=6
# each attempt random number genrated
# random number genrate sum
# fix_value=150

# fix_value=150
# total=0
# for i in range(6):
#     num=random.randint(20,30)
#     total+=num
# print(total)
# if total==150:
#     print("no is match")
# elif 140 <= total <=175:
#     print("nearest")
# else:
#     print("to far")

# sample()
# shuffle()
# emp_name=["aman", "kamal","deepak","shivam"]
# res=random.sample(emp_name,k=2)
# print(res)

# emp_name=["aman", "kamal","deepak","shivam"]
# res=random.shuffle(emp_name)
# print(emp_name)

# coupon code
# CXYZ9876

# def generate_coupon():
#     a_to_z="abcdefghijklmnopqrstuvwxyz"
#     num="1234567890"

#     char=[random.choice(a_to_z).upper() for i in range(1,5)]
#     num=[random.choice(num)for i in range(1,5)]

#     print("".join(char+num))
# for i in range(1,11):
#     generate_coupon()

def generate_coupon():
    a_to_z="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"

    char="".join(random.choices(a_to_z,k=4))
    num=random.random()*10000

    res=char.upper()+str(int(num))
    print(res)
for i in range(1,11):
    generate_coupon()

def generate_coupon():
    import string
    print(random.choices(string)