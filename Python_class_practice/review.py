# filter into review.txt file only positive comment and good_product
review=[
    {"negative": "this is very bad product i ordered last one month ago",
     "positive":" this product is very nice go for it",
    "bad_product": ["shoe","cricket bat"],
    "good_product":["books","mobile phone"]
    }
]
file = open("review.txt", "w")
for i in review:
    for key , val in i.items():
       if key =="positive" or key=="good_product":
        file.write(f"{key},{val}\n")
       elif key=="negative" or key=="bad_product":
          file.write(f"{key},{val}\n")
          

file.close()
print("Data saved successfully in review.txt")

# for i in review:
#     for key in i.keys():
#         print(key)

#     query=f""" create table if not exist product_review
#     {key[0]} varchar(100),
#      {key[1]}
# """
# file = open ("review.txt","w")
# for i in review:
#     file.write("Negetive review:\n")
#     file.write(i["negative"] + "\n\n")
#     file.write("bad_product:\n")
#     for product in i["bad_product"]:
#         file.write(product + "\n")
# file.close()
# print("Data saved successfully in review.txt")
